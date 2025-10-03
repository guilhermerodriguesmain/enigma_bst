# tests/test_ascii_converter.py

import pytest
from modules.ascii_converter import AsciiConverter

@pytest.fixture
def converter():
    """Fornece uma instância limpa da classe AsciiConverter para cada teste."""
    return AsciiConverter()

# --- Testes de Unidade para Conversões Individuais ---

@pytest.mark.parametrize("char, expected_code", [
    ('A', 65),
    ('z', 122),
    ('0', 48),
    ('!', 33),
    (chr(0), 0),
    (' ', 32),
])
def test_to_ascii(converter, char, expected_code):
    """Verifica a conversão de um único caractere para seu código ASCII."""
    assert converter.to_ascii(char) == expected_code

@pytest.mark.parametrize("code, expected_char", [
    (65, 'A'),
    (122, 'z'),
    (48, '0'),
    (33, '!'),
    (0, chr(0)),
    (32, ' '),
])
def test_from_ascii(converter, code, expected_char):
    """Verifica a conversão de um único código ASCII para seu caractere."""
    assert converter.from_ascii(code) == expected_char

# --- Testes para Casos Inválidos ---

def test_to_ascii_invalid_char(converter):
    """
    Verifica se caracteres fora da tabela ASCII (0-255) ou strings longas
    retornam 0, conforme a lógica .get(key, 0).
    """
    assert converter.to_ascii('€') == 0  # Caractere Unicode fora da faixa
    assert converter.to_ascii('AB') == 0 # String com mais de um caractere

def test_from_ascii_invalid_code(converter):
    """
    Verifica se códigos fora da faixa 0-255 retornam 0,
    conforme a lógica .get(key, 0).
    """
    assert converter.from_ascii(300) == 0
    assert converter.from_ascii(-1) == 0

# --- Teste de Ciclo Completo (Round-Trip) para Múltiplos Itens ---

@pytest.mark.parametrize("original_chars", [
    (['H', 'e', 'l', 'l', 'o']),
    (['P', 'y', 't', 'h', 'o', 'n', ' ', '3', '.','1', '2']),
    (['$', '%', '*', '(', ')']),
    ([chr(0), chr(127), chr(255)]), # Testando limites da tabela
    ([]), # Testando lista vazia
])
def test_multiple_conversion_roundtrip(converter, original_chars):
    """
    Garante que a conversão de uma lista de caracteres para ASCII e de
    volta para caracteres resulta na lista original. ✅
    """
    # Act
    ascii_codes = converter.convert_multiple_to_ascii(original_chars)
    result_chars = converter.convert_multiple_from_ascii(ascii_codes)
    
    # Assert
    assert result_chars == original_chars