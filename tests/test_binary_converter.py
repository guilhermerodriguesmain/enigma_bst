# tests/test_binary_converter.py

import pytest
from modules.binary_converter import BinaryConverter

@pytest.fixture
def converter():
    """Fornece uma instância da classe BinaryConverter para cada teste."""
    return BinaryConverter()

# --- Testes para Métodos de Inteiros (encrypt/decrypt) ---

@pytest.mark.parametrize("original_list", [
    ([10, 42, 255]),
    ([0]),
    ([i for i in range(16)]) # Lista de 0 a 15
])
def test_integer_roundtrip(converter, original_list):
    """
    Verifica se a conversão de inteiros para binário e de volta
    resulta na lista original.
    """
    # Act
    encrypted = converter.encrypt(original_list)
    decrypted = converter.decrypt(encrypted)
    
    # Assert
    assert decrypted == original_list

def test_encrypt_format(converter):
    """Verifica se o formato binário para inteiros (08b) está correto."""
    # 10 em binário é 1010. Com 8 bits, deve ser '00001010'.
    assert converter.encrypt([10]) == ['00001010']
    # 0 deve ser '00000000'
    assert converter.encrypt([0]) == ['00000000']

# --- Testes para Métodos de Floats (float_bin_converter/bin_float_converter) ---

@pytest.mark.parametrize("original_list", [
    ([10.5, 0.25]),                  # Números com representação binária finita
    ([123.0, 45.0]),                 # Números sem parte fracionária
    ([0.0]),                         # Caso do zero
    ([3.14159]),                     # Número com representação binária infinita
    ([0.1, 0.2, 0.7])                # Outros casos de imprecisão
])
def test_float_roundtrip(converter, original_list):
    """
    Verifica se a conversão de floats para binário e de volta
    resulta em uma lista aproximadamente igual à original.
    """
    # Act
    binary_strings = converter.float_bin_converter(original_list)
    converted_floats = converter.bin_float_converter(binary_strings)

    # Assert
    # Usamos pytest.approx para comparar floats devido a possíveis imprecisões.
    assert converted_floats == pytest.approx(original_list)

def test_float_bin_converter_format(converter):
    """Verifica o formato da string binária customizada para floats."""
    # 10.5 -> 10 é '1010', 0.5 é '1' -> '1010#1'
    assert converter.float_bin_converter([10.5]) == ['1010#1']
    # 0.75 -> 0 é '', 0.75 é '11' -> '#11' (implementação atual resulta em '0#11')
    assert converter.float_bin_converter([0.75]) == ['0#11']
    # 12.0 -> '1100' (sem parte fracionária, sem '#')
    assert converter.float_bin_converter([12.0]) == ['1100']