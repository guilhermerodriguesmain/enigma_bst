# tests/test_IntegralProcessor.py

import pytest
from modules.IntegralProcessor import IntegralProcessor

@pytest.fixture
def processor():
    """Fornece uma instância da classe para ser usada em cada teste."""
    return IntegralProcessor()

# --- Testes para o método encrypt ---

def test_encrypt_basic(processor):
    """Testa a criptografia com valores simples e chave conhecida."""
    # A fórmula é: integral = (num * key^2) / 2
    # Para num=10, key=2 -> (10 * 2^2) / 2 = 20.0
    # Para num=20, key=4 -> (20 * 4^2) / 2 = 160.0
    
    numbers = [10, 20]
    key = 2
    expected = [20.0, 80.0] # CORREÇÃO: Ambos usam a mesma chave
    # Para num=10, key=2 -> (10 * 4) / 2 = 20.0
    # Para num=20, key=2 -> (20 * 4) / 2 = 40.0
    expected_corrected = [20.0, 40.0]

    assert processor.encrypt(numbers, key) == expected_corrected

def test_encrypt_empty_list(processor):
    """Testa se uma lista vazia de entrada resulta em uma lista vazia de saída."""
    assert processor.encrypt([], key=5) == []

# --- Testes para o método decrypt ---

def test_decrypt_basic(processor):
    """Testa a descriptografia com valores simples e chave conhecida."""
    # A fórmula é: num = (2 * R) / (key^2)
    # Para R=20.0, key=2 -> (2 * 20) / 4 = 10
    # Para R=40.0, key=2 -> (2 * 40) / 4 = 20
    
    encrypted_numbers = [20.0, 40.0]
    key = 2
    expected = [10, 20]
    
    assert processor.decrypt(encrypted_numbers, key) == expected

def test_decrypt_key_zero_raises_error(processor):
    """Verifica se o método decrypt levanta um erro ao usar chave 0."""
    with pytest.raises(ZeroDivisionError):
        processor.decrypt([10, 20], key=0)

# --- Teste de ciclo completo (Round-trip) ---

@pytest.mark.parametrize("original_list, key", [
    ([10, 20, 30], 2),            # Lista simples, chave inteira
    ([1, 2, 3, 5, 8, 13], 10),    # Lista maior, chave maior
    ([100], 1),                   # Lista com um elemento
    ([5, 0, 15], 3)               # Lista contendo zero
])
def test_encrypt_decrypt_roundtrip(processor, original_list, key):
    """
    Verifica se a descriptografia do resultado da criptografia
    retorna a lista original. Este é o teste mais importante.
    """
    # Act
    encrypted_data = processor.encrypt(original_list, key)
    decrypted_data = processor.decrypt(encrypted_data, key)
    
    # Assert
    assert decrypted_data == original_list