# ASCII Converter Module

class AsciiConverter:
    def __init__(self):
        self.ascii_table = {chr(i): i for i in range(256)}
        self.ascii_table.update({i: chr(i) for i in range(256)})

    def to_ascii(self, char): # converte caractere para ASCII decimal
        return self.ascii_table.get(char, 0)
    
    def from_ascii(self, code): # converte ASCII decimal para caractere
        return self.ascii_table.get(code, 0)

    def convert_multiple_to_ascii(self, chars): # converte multiplos caracteres para ASCII decimal
        return [self.to_ascii(c) for c in chars]

    def convert_multiple_from_ascii(self, codes): # converte multiplos ASCII decimais para caracteres
        return [self.from_ascii(c) for c in codes]
    

