import json

class JsonExporter:
    def __init__(self, values):
        self.values = values

    def export_to_json(self, file_name):
        """Exporta os valores para um arquivo JSON de forma legível."""
        try:
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(self.values, json_file, indent=4, ensure_ascii=False)
            print(f"Valores exportados para {file_name} em formato JSON.")
        except Exception as e:
            print(f" Erro ao exportar para JSON: {e}")
