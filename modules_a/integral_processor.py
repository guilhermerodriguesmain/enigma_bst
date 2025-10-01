# Integral Processor Module

"""
Realiza calculos integrais simples em uma lista de números inteiros usando orientação a objetos
para usar este módulo é necessário passar uma lista de números inteiros como parâmetro para o método encrypt ou decrypt

métodos : encrypt - retorna uma lista de números encriptados
            decrypt - retorna uma lista de números decriptados

"""
import sympy as sp

class IntegralProcessor:
    def __init__(self):
        self.x = sp.symbols('x')
    
    def encrypt(self, numbers):
        encripted = []
        for num in numbers:
            f = num * self.x
            integral = sp.integrate(f, (self.x, 0, (numbers.index(num)+1)))
            encripted.append(float(integral))
        return encripted
    
    def decrypt(self, numbers):
        decripted = []
        for i, R in enumerate(numbers, start=1):
            n = int((2 * R) / (i**2))  
            decripted.append(n)
        return decripted
    
# exemplo de uso
"""
if __name__ == "__main__":
    processor = IntegralProcessor()
    
    original_numbers = [65,66,67]
    print(f"Original Numbers: {original_numbers}")
    
    encrypted_numbers = processor.encrypt(original_numbers)
    print(f"Encrypted Numbers: {encrypted_numbers}")
    
    decrypted_numbers = processor.decrypt(encrypted_numbers)
    print(f"Decrypted Numbers: {decrypted_numbers}")  
"""
# #fim do código   
# versão 1.0
# data 2025-09-30