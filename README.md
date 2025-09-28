# Enigma-BST 
Sistema de Criptografia Didática com Árvores Binárias

## Resumo
Projeto acadêmico que implementa um sistema de criptografia modularizado inspirado na máquina Enigma.  
Utiliza **árvores binárias de busca (BST)** como mecanismo de embaralhamento, com fluxo de encriptação (Grupo A) e decriptação (Grupo B).  

O sistema é **gamificado**: o Grupo A gera mensagens encriptadas em JSON e o Grupo B deve decodificá-las com base na seed e no algoritmo inverso.

---

## Objetivos
- Exercitar modularização de código em Python.
- Aplicar estruturas de dados (árvores binárias).
- Trabalhar com manipulação de dados e criptografia didática.
- Usar boas práticas de versionamento e documentação.

---

## Tecnologias
- **Python 3.13**
- **VS Code**
- **Git + GitHub**
- **Bibliotecas**:
  - 
---

## 📂 Estrutura do Projeto

enigma/
│
├── modules/
│   ├── __init__.py
│
│   # Grupo A - Encriptação
│   ├── ascii_converter.py          # String → ASCII decimal
│   ├── integral_processor.py       # Aplica integral
│   ├── binary_converter.py         # Decimal → Binário
│   ├── binary_tree_handler.py      # Embaralha binários via árvore
│   ├── json_exporter.py            # Gera JSON + exporta
│
│   # Grupo B - Decodificação
│   ├── json_reader.py              # Lê JSON + seed
│   ├── binary_tree_rebuilder.py    # Reconstrói ordem da árvore
│   ├── binary_to_decimal.py        # Binário → Decimal
│   ├── integral_inverse.py         # Aplica fórmula inversa
│   └── ascii_rebuilder.py          # Decimal → String original
│
├── main.py
├── requirements.txt
├── README.md
└── docs/
    └── projeto.pdf

