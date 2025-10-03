# tests/test_Tree.py

import pytest
from modules.Tree import Tree # Importa a classe Tree do seu módulo

# Uma "fixture" do pytest. Esta função será executada antes de cada teste
# que a solicitar. Ela garante que cada teste comece com uma árvore nova e vazia.
@pytest.fixture
def empty_tree():
    """Fornece uma instância limpa da árvore para cada teste."""
    return Tree()

# ----------------- Testes para pos_order_insert -----------------
# A lógica aqui é: se construirmos a árvore a partir de uma mensagem
# em pós-ordem, a travessia em pós-ordem resultante deve ser idêntica
# à mensagem original.

def test_pos_order_insert_string_impar(empty_tree):
    """
    Testa a inserção pós-ordem com uma string de tamanho ímpar.
    """
    message = "DATAS"
    empty_tree.pos_order_insert(message)
    # A lista de travessia pós-ordem deve ser igual aos caracteres da mensagem original
    assert empty_tree.post_order_list() == list(message)

def test_pos_order_insert_string_par(empty_tree):
    """
    Testa a inserção pós-ordem com uma string de tamanho par.
    """
    message = "PYTHON"
    empty_tree.pos_order_insert(message)
    assert empty_tree.post_order_list() == list(message)

def test_pos_order_insert_string_vazia(empty_tree):
    """
    Testa a inserção com uma string vazia.
    A árvore deve permanecer vazia (raiz None).
    """
    empty_tree.pos_order_insert("")
    assert empty_tree.root is None
    assert empty_tree.post_order_list() == []

def test_pos_order_insert_string_um_caractere(empty_tree):
    """
    Testa a inserção com apenas um caractere.
    """
    message = "A"
    empty_tree.pos_order_insert(message)
    assert empty_tree.post_order_list() == ['A']
    assert empty_tree.root.value == 'A'
    assert empty_tree.root.left is None
    assert empty_tree.root.right is None

# ----------------- Testes para crypto_insert (construção pré-ordem) -----------------
# A lógica aqui é: se construirmos uma árvore a partir de uma lista em
# pré-ordem (usando crypto_insert), a travessia em pós-ordem terá uma
# sequência específica e previsível, que podemos verificar.

def test_crypto_insert_happy_path(empty_tree):
    """
    Testa a inserção pré-ordem com uma lista de valores complexa.
    O resultado esperado é a travessia em pós-ordem da árvore resultante.
    Árvore Esperada:
          F
       /     \
      B       E
     / \     / \
    A   D   G   I
       /       /
      C       H
    """
    pre_order_values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    expected_post_order = ['A', 'C', 'D', 'B', 'G', 'H', 'I', 'E', 'F']
    
    empty_tree.crypto_insert(pre_order_values)
    
    assert empty_tree.post_order_list() == expected_post_order

def test_crypto_insert_lista_simples(empty_tree):
    """
    Testa a inserção pré-ordem com uma lista de 3 elementos.
    Árvore Esperada:
          A
         / \
        B   C
    """
    pre_order_values = ['A', 'B', 'C']
    expected_post_order = ['B', 'C', 'A'] # Pós-ordem: esquerda, direita, raiz
    
    empty_tree.crypto_insert(pre_order_values)
    
    assert empty_tree.post_order_list() == expected_post_order

def test_crypto_insert_lista_vazia(empty_tree):
    """
    Testa a inserção com uma lista vazia.
    A árvore deve permanecer vazia.
    """
    empty_tree.crypto_insert([])
    assert empty_tree.root is None
    assert empty_tree.post_order_list() == []

def test_crypto_insert_lista_um_elemento(empty_tree):
    """
    Testa a inserção com uma lista de um único elemento.
    """
    values = ['ROOT']
    empty_tree.crypto_insert(values)
    assert empty_tree.post_order_list() == ['ROOT']
    assert empty_tree.root.value == 'ROOT'
    assert empty_tree.root.left is None
    assert empty_tree.root.right is None