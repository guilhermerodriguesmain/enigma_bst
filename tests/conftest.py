# tests/conftest.py

import sys
import os

# Adiciona o diretório raiz do projeto (a pasta que contém 'modules' e 'tests')
# ao caminho de busca do Python.
# Isso permite que os testes importem os módulos de forma limpa, como:
# from modules.arvore import Tree

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))