import json

class JsonExporter:
    def __init__(self, tree_values, public_key):
        
        self.tree_values = tree_values
        self.public_key = public_key

    def export_to_json(self, file_name):
        data_to_export = {
            "public_key": self.public_key,
            "tree_post_order": self.tree_values
        }

        with open(file_name, 'w') as json_file:
            json.dump(data_to_export, json_file, indent=4)
            print(f"Valores exportados para {file_name} em formato JSON.")
