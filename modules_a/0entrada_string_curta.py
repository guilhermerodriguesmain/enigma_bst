# List_string_converter Module
# deve ser capaz de receber uma string curta (até 10 caracteres)
# deve ser capaz de ler um aruvivo de texto longo
# e transformar em uma lista de caracteres
# usando orientação a objetos
# e retornar uma lista de seus caracteres individuais
class TXT_reader:
    def __init__(self, filename):
        self.filename = filename

    def read_string(self):
        with open(self.filename, 'r') as file:
            content = file.read().strip()
            if len(content) > 10:
                raise ValueError("A string no arquivo deve ter no máximo 10 caracteres.")
            return list(content)
        
# Exemplo de uso do leitor de arquivo
if __name__ == "__main__":
    try:
        reader = TXT_reader('D:\\FACULDADE\\Periodos\\quarto_periodo\\EDA\\p1\\enigma\\modules_a\\input.txt')
        chars = reader.read_string()
        print(f"Characters from file: {chars}")
    except Exception as e:
        print(e)
        
def entrada_string_curta(s):
    if len(s) >= 0 and len(s) > 30:
        raise ValueError("A string deve ter no máximo 10 caracteres.")
    return list(s)

# Exemplo de uso
if __name__ == "__main__":
    try:
        s = "Hello Paython"
        chars = entrada_string_curta(s)
        print(f"String: {s} -> Characters: {chars}")
        
        s_long = "This string is too long"
        chars_long = entrada_string_curta(s_long)
        print(f"String: {s_long} -> Characters: {chars_long}")
    except ValueError as e:
        print(e)
# fim do código
# feito com ajuda de chatGPT
# versão 2.0
# data 2025-09-28
