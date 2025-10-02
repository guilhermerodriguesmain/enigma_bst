import sympy as sp

class IntegralProcessor:
    def __init__(self):
        self.x = sp.symbols('x')
    
    def encrypt(self, numbers, key):
        encripted = []
        for i, num in enumerate(numbers, start=1):
            f = num * self.x
            integral = sp.integrate(f, (self.x, 0, key))  # ∫ num*x dx de 0 até i
            encripted.append(float(integral))
        return encripted
    
    def decrypt(self, numbers,key):
        decripted = []
        for i, R in enumerate(numbers, start=1):
            n = int((2 * R) / (key**2))   # inverte a fórmula R = num*i²/2
            decripted.append(n)
        return decripted


# exemplo de uso
if __name__ == "__main__":
    processor = IntegralProcessor()
    
    original_numbers = [65,66,67,65]  # testando com número repetido
    print(f"Original Numbers: {original_numbers}")
    
    encrypted_numbers = processor.encrypt(original_numbers)
    print(f"Encrypted Numbers: {encrypted_numbers}")
    
    decrypted_numbers = processor.decrypt(encrypted_numbers)
    print(f"Decrypted Numbers: {decrypted_numbers}")  
