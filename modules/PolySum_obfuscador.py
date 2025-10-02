from math import isqrt

class LogExpObfuscator:
    """
    Obfuscador baseado em exponenciação modular e log discreto.
    - key = (p, g), onde p é primo > 255 e g é um gerador módulo p.
    - Entrada/saída: lista de inteiros ASCII (0..255).
    """
    
    def __init__(self, key):
        self.p = 257
        self.g = key
        if self.p <= 255:
            raise ValueError("p deve ser > 255")
        if not isinstance(self.g, int) or not (1 < self.g < self.p):
            raise ValueError("g deve ser inteiro no intervalo (1, p)") # o que é p
    
    def _discrete_log_bsgs(self, g, h, p):
        """
        Resolve g^x ≡ h (mod p) usando Baby-step Giant-step.
        Retorna x (inteiro).
        """
        m = isqrt(p - 1) + 1

        # baby steps
        table = {}
        e = 1
        for j in range(m):
            if e not in table:  # guarda o menor expoente
                table[e] = j
            e = (e * g) % p

        # fator g^-m
        g_m = pow(g, m, p)
        g_m_inv = pow(g_m, -1, p)

        gamma = h
        for i in range(m):
            if gamma in table:
                return i * m + table[gamma]
            gamma = (gamma * g_m_inv) % p
        raise ValueError("log discreto não encontrado")
    
    def encrypt(self, ascii_list):
        out = []
        for n in ascii_list:
            E = pow(self.g, n, self.p)  # g^n mod p
            cipher = (E - 1) % 256       # mapeia para byte 0..255
            out.append(cipher)
        return out
    
    def decrypt(self, encrypted_list):
        out = []
        for b in encrypted_list:
            E = (b + 1) % self.p
            n = self._discrete_log_bsgs(self.g, E, self.p)
            out.append(n)
        return out


# ---------------- EXEMPLO -----------------
if __name__ == "__main__":
    # chave: (p, g)
    key = (257, 3)   # 257 é primo > 255, 3 é gerador
    obfuscator = LogExpObfuscator(key)

    # ASCII da palavra "ABC"
    original_ascii = [65, 66, 67]
    print("Original:", original_ascii)

    encrypted = obfuscator.encrypt(original_ascii)
    print("Encrypted:", encrypted)

    decrypted = obfuscator.decrypt(encrypted)
    print("Decrypted:", decrypted)
