
from typing import Any

class BinarioDecoder:
    """Classe para conversão e descriptografia de números binários."""

    @staticmethod
    def binario_para_decimal(b: str) -> int:
        """Converte binário (com ou sem fração) para decimal arredondado."""
        if '.' in b:
            parte_int, parte_frac = b.split('.')
            dec_int = int(parte_int, 2) if parte_int else 0
            dec_frac = sum(int(bit) * 2**(-i-1) for i, bit in enumerate(parte_frac))
            return round(dec_int + dec_frac)
        else:
            return int(b, 2)

    def descriptografar_binario(self, bin_str: str) -> list[int]:
        """Recebe string binária e retorna lista de decimais arredondados."""
        try:
            bin_str = bin_str.strip().replace('\n', ' ').replace('\r', ' ')
            partes = bin_str.split()
            return [self.binario_para_decimal(b) for b in partes if all(c in '01.' for c in b)]
        except Exception:
            return []

    def decodificar_json(self, dado: Any) -> Any:
        """Percorre JSON e descriptografa strings binárias."""
        if isinstance(dado, str):
            return self.descriptografar_binario(dado)
        elif isinstance(dado, list):
            return [self.decodificar_json(item) for item in dado]
        elif isinstance(dado, dict):
            return {k: self.decodificar_json(v) for k, v in dado.items()}
        return dado


# ----------------- TESTE -----------------
if __name__ == "__main__":
    decoder = BinarioDecoder()

    s1 = "1101 101.1 10.06"
    print("Teste string:", s1)
    print("Decimal arredondado:", decoder.descriptografar_binario(s1))  # [13, 6, 2]

    s2 = ["101", "111.01"]
    print("Teste JSON:", s2)
    print("Decimal arredondado:", decoder.decodificar_json(s2))  # [[5], [7]]
