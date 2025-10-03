# tests/test_input_text.py

import pytest
import json
from modules.input_text import ListStringConverter

# --- Testes para o método convert_json ---

def test_convert_json_success(tmp_path):
    """
    Verifica se o método lê um JSON válido e retorna os dados corretamente.
    """
    # Arrange: Prepara o ambiente do teste
    file_path = tmp_path / "input.json"
    test_data = {
        "public_key": {"e": 123, "n": 456},
        "tree_post_order": [10, 20, 30]
    }
    # Escreve o conteúdo de teste no arquivo temporário
    file_path.write_text(json.dumps(test_data), encoding='utf-8')
    
    converter = ListStringConverter(file_path)

    # Act: Executa o método a ser testado
    public_key, tree_values = converter.convert_json()

    # Assert: Verifica se o resultado é o esperado
    assert public_key == test_data["public_key"]
    assert tree_values == test_data["tree_post_order"]

def test_convert_json_missing_key(tmp_path):
    """
    Verifica o comportamento quando a chave 'tree_post_order' não existe no JSON.
    O método deve retornar uma lista vazia por padrão.
    """
    # Arrange
    file_path = tmp_path / "input_missing_key.json"
    test_data = {"public_key": {"e": 789, "n": 101}}
    file_path.write_text(json.dumps(test_data), encoding='utf-8')
    
    converter = ListStringConverter(file_path)

    # Act
    public_key, tree_values = converter.convert_json()

    # Assert
    assert public_key == test_data["public_key"]
    assert tree_values == [] # O valor padrão deve ser uma lista vazia

# --- Testes para o método convert ---

def test_convert_text_to_char_list(tmp_path):
    """
    Verifica se o método converte o conteúdo de um arquivo de texto
    em uma lista de caracteres.
    """
    # Arrange
    file_path = tmp_path / "input.txt"
    content = "Olá"
    file_path.write_text(content, encoding='utf-8')
    
    converter = ListStringConverter(file_path)

    # Act
    char_list = converter.convert()

    # Assert
    assert char_list == ['O', 'l', 'á']

def test_convert_empty_file(tmp_path):
    """
    Verifica o comportamento do método 'convert' com um arquivo vazio.
    """
    # Arrange
    file_path = tmp_path / "empty.txt"
    file_path.touch() # Cria um arquivo vazio
    
    converter = ListStringConverter(file_path)

    # Act
    char_list = converter.convert()

    # Assert
    assert char_list == []

# --- Testes para o método caracter_to_text ---

def test_caracter_to_text(tmp_path):
    """
    Verifica se o método escreve corretamente uma lista de caracteres em um arquivo de saída.
    """
    # Arrange
    # O arquivo de entrada não é usado por este método, mas o __init__ exige um.
    dummy_input_path = tmp_path / "dummy.txt"
    converter = ListStringConverter(dummy_input_path)
    
    char_list = ['P', 'y', 't', 'h', 'o', 'n']
    output_file_base = tmp_path / "output_file"
    expected_output_path = tmp_path / "output_file.txt"

    # Act
    converter.caracter_to_text(char_list, output_file_base)

    # Assert
    assert expected_output_path.exists()
    assert expected_output_path.read_text(encoding='utf-8') == "Python"