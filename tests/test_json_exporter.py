# tests/test_json_exporter.py

import json
import pytest
from modules.json_exporter import JsonExporter # Importa a sua classe

def test_export_to_json(tmp_path):
    """
    Testa se a classe JsonExporter exporta corretamente os dados para um arquivo JSON.
    Usa a fixture 'tmp_path' do pytest para criar um arquivo em um diretório temporário.
    """
    # 1. Preparação (Arrange)
    # Define os dados de entrada para o teste
    test_key = {"e": 65537, "n": 123456789}
    test_values = [10, 25, 5, 30, 15]
    
    # Cria a instância da classe que queremos testar
    exporter = JsonExporter(tree_values=test_values, public_key=test_key)
    
    # Define o caminho completo do arquivo de saída dentro do diretório temporário
    output_file = tmp_path / "data.json"

    # 2. Execução (Act)
    # Chama o método que queremos testar
    exporter.export_to_json(output_file)

    # 3. Verificação (Assert)
    # Verifica se o arquivo foi realmente criado
    assert output_file.exists(), "O arquivo JSON não foi criado."

    # Abre o arquivo criado e carrega seu conteúdo para verificação
    with open(output_file, 'r') as f:
        data_from_file = json.load(f)

    # Verifica se o conteúdo do arquivo é exatamente o que esperamos
    expected_data = {
        "public_key": test_key,
        "tree_post_order": test_values
    }
    assert data_from_file == expected_data, "O conteúdo do arquivo JSON está incorreto."