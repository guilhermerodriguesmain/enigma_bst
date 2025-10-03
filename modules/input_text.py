# List_string_converter Module

import json
class ListStringConverter:
    def __init__(self, filename):
        self.filename = filename

    def convert_json(self):
        
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
        with open((str(output_file) + '.txt'), 'w', encoding='utf-8') as file:
            file.write("".join(str(c) for c in char_list))
        print(f"Conteúdo salvo em {output_file}.txt")
