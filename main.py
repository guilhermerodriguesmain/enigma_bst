# Enigma project main module

# Este módulo integra vários módulos de processamento para demonstrar sua funcionalidade.

# Importa os módulos necessários
from modules.input_text import ListStringConverter # Módulo para converter texto em lista de caracteres
from modules.ascii_converter import AsciiConverter # Módulo para converter caracteres em valores ASCII e vice-versa
from modules.integral_processor import IntegralProcessor # Módulo para realizar cálculos integrais simples
#from enigma.modules.binary_converter import BinaryConverter # Módulo para converter números entre binário e decimal
from modules.Tree import Tree # Módulo para manipulação de árvores
from tkinter import Tk, filedialog

def main_ecripting(a):
    # Passo 1: Ler o arquivo de texto e converter para uma lista de caracteres
    input_text= ListStringConverter(a)
    char_list = input_text.convert()
    
    # Passo 2: Converter a lista de caracteres para seus valores ASCII decimais
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(char_list)
    
    
    # Passo 3: Realizar cálculos integrais simples nos valores ASCII
    integral_processor = IntegralProcessor()
    print(integral_processor.encrypt(ascii_values))
    
    # Passo 4: Converter os valores integrais para binário
    
    # passo 5: Montar a árvore binária em pós ordem com os valores binários
    
    # passo 6: exportar a árvore em pós ordem para um arquivo txt em formato JSON
    
def main_decripting(a):
    # Passo 1: Ler o arquivo txt com a árvore em pós ordem em formato JSON e montar a árvore binária
    
    
    # Passo 2: Percorrer a árvore em pós ordem e salvar os valores em uma lista
    
    
    # Passo 3: Converter os valores binários para decimais
    
    
    # Passo 4: Realizar o processo inverso dos cálculos integrais para obter os valores ASCII originais
    integral_processor = IntegralProcessor()
    ascii_values = integral_processor.decrypt(decimal_values)
    
    # Passo 5: Converter os valores ASCII de volta para caracteres
    ascii_converter = AsciiConverter()
    char_list = ascii_converter.convert_multiple_from_ascii(ascii_values)
    
    # Passo 6: Juntar a lista de caracteres em uma string e salvar em um arquivo de texto
    
    
# execução 

if __name__ == "__main__":
    Tk().withdraw()  # esconde a janela principal
    caminho = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Text files", "*.txt")])
    main_ecripting(caminho)
    
# main_decripting('tree_output.txt')