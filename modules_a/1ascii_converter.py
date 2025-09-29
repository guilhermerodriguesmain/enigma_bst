# ASCII Converter Module
# criado um converor de caracteres para ASCII decimal e vice-versa
# usando orientação a onjetos
# criar dicionario ou iterador para conversão
# deve ser capaz de converter multiplos caracteres simultaneos em uma nova lista de seus equivalentes decimais

### para usar estte módulo é necessario transformar uma string em uma lista de caracteres e passar como parametro para o método convert_multiple_to_ascii
# retorna uma liesta de inteiros

class AsciiConverter:
    def __init__(self):
        self.ascii_table = {chr(i): i for i in range(128)}
        self.ascii_table.update({i: chr(i) for i in range(128)})

    def to_ascii(self, char): # converte caractere para ASCII decimal
        return self.ascii_table.get(char, None)

    def from_ascii(self, code): # converte ASCII decimal para caractere
        return self.ascii_table.get(code, None)

    def convert_multiple_to_ascii(self, chars): # converte multiplos caracteres para ASCII decimal
        return [self.to_ascii(c) for c in chars]

    def convert_multiple_from_ascii(self, codes): # converte multiplos ASCII decimais para caracteres
        return [self.from_ascii(c) for c in codes]

# Exemplo de uso
if __name__ == "__main__":
    converter = AsciiConverter()
    
    char = 'B'
    ascii_code = converter.to_ascii(char)
    print(f"Character: {char} -> ASCII: {ascii_code}")
    
    code = 70
    character = converter.from_ascii(code)
    print(f"ASCII: {code} -> Character: {character}")

    chars = ['A', 'B', 'C']
    ascii_codes = converter.convert_multiple_to_ascii(chars)
    print(f"Characters: {chars} -> ASCII: {ascii_codes}")

    codes = [65, 66, 67]
    characters = converter.convert_multiple_from_ascii(codes)
    print(f"ASCII: {codes} -> Characters: {characters}")

#fim do código   
# feito com ajuda de chatGPT
# versão 1.0
# data 2025-09-28
