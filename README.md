# Enigma-BST 
Sistema de Criptografia Didática com Árvores Binárias

## Resumo
Projeto acadêmico que implementa um sistema de criptografia modularizado inspirado na máquina Enigma.  
Utiliza **árvores binárias de busca (BST)** como mecanismo de embaralhamento, com fluxo de encriptação (Grupo A) e decriptação (Grupo B).  

O sistema é **gamificado**: o Grupo A gera mensagens encriptadas em JSON e o Grupo B deve decodificá-las com base na seed e no algoritmo inverso.

---------------------------------------------------------------------------------------------------

## Objetivos
- Exercitar modularização de código em Python.
- Aplicar estruturas de dados (árvores binárias).
- Trabalhar com manipulação de dados e criptografia didática.
- Usar boas práticas de versionamento e documentação.

---------------------------------------------------------------------------------------------------------------------

## Tecnologias
- **Python 3.13**
- **VS Code**
- **Git + GitHub**
- **Bibliotecas**:
    * SymPy: Para os cálculos matemáticos na etapa da integral.

    * Tkinter: Para a seleção de arquivos de forma gráfica (parte da biblioteca padrão do Python).

    * Pytest: Para a suíte de testes unitários e de integração.

    * Pytest-Mock: Plugin para simular comportamentos durante os testes.

--------------------------------------------------------------------------------------------------------

## Estrutura do Projeto

enigma/
│
├── docs/
│    ├── orientacao.txt
│    └── projeto.pdf
│
├── modules/
│   ├── __init__.py
│   ├── ascii_converter.py          # String → ASCII decimal → String
│   ├── IntegralProcessor.py       # Aplica integral
│   ├── binary_converter.py         # Decimal → Binário → Decimal
│   ├── input_text.py             # recebe a e entrada de texto
│   ├── Tree.py                    # criação e desmonte da árvore
│   └── json_exporter.py            # Gera JSON + exporta
│      
├── tests/
│    ├── __init__.py
│    ├── conftest.py
│    ├── test_ascii_convertes.py
│    ├── test_binary_converter.py
│    ├── test_input_text.py
│    ├── test_IntegralProcessor.py
│    ├── test_json_exporter.py
│    ├── test_Tree.py
│    └── test_main_integration.py
│    
├── .gitignore
├── main.py
├── README.md
└── requirements.txt 

## Instalação e Configuração

1 - Clone ou baixe este repositório;
2 - Crie um ambiente virtual (recomendado);
3 - Instale as dependências contidas no arquivo requeriments.txt;

## Como usar

1 - Execute o script principal (main.py);
2 - Siga as instruções do menu;
3 - O arquivo de saída criptografado (tree_output.json) será gerado na mesma pasta. Ao descriptografar, você poderá nomear o arquivo de texto final.



