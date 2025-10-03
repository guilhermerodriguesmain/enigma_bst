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
        """Lê o arquivo JSON e retorna a chave pública e a lista da árvore."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            data = json.loads(content)

            public_key = data.get("public_key")
            tree_post_order = data.get("tree_post_order", [])

            return public_key, tree_post_order

    def convert(self):
        
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return list(content)
    
    def caracter_to_text(self, char_list, output_file):
        with open(str(output_file + '.txt'), 'w', encoding='utf-8') as file:
            file.write("".join(str(c) for c in char_list))
        print(f"Conteúdo salvo em {output_file}.txt")

#Exemplo de uso
if __name__ == "__main__":
    converter = ListStringConverter()
    char_list = converter.convert()
    print(f"Character List: {char_list}")
    
#    json_list = converter.convert_json()
#    print(f"JSON List: {json_list}")

# fim do código
# feito com ajuda de chatGPT
# versão 3.0
# data 2025-09-29
