# Módulo para exportar a árvore em formato JSON
# deve receber uma lista e exportar para um arquivo txt em formato JSON
""" Exportar uma lista de valores para um arquivo em formato JSON """
import json
class JsonExporter:
    def __init__(self, values):
        self.values = values

    def export_to_json(self, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(self.values, json_file)
            print(f"Valores exportados para {file_name} em formato JSON.")
