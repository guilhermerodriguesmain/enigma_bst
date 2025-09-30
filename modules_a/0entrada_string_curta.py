# List_string_converter Module
"""
Itera sobre um arquivo de texto e converte seu conteúdo em uma lista de caracteres ou interpreta o conteúdo como uma lista em formato JSON usando orientação a objetos

para usar este módulo é necessário passar o local do arquivo como parâmetro para o método convert ou convert_json

métodos : convert - retorna uma lista de caracteres
          convert_json - retorna uma lista interpretada de um formato JSON
"""
import json
class ListStringConverter:
    def __init__(self, filename):
        self.filename = filename

    def convert_json(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return json.loads(content)

    def convert(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return list(content)

# fim do código
# feito com ajuda de chatGPT
# versão 3.0
# data 2025-09-29
