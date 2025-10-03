# Enigma project main module

# Este módulo integra vários módulos de processamento para demonstrar sua funcionalidade.

# Importa os módulos necessários
from modules.Input_text import ListStringConverter 
from modules.Ascii_converter import AsciiConverter 
from modules.IntegralProcessor import IntegralProcessor
from modules.Binary_converter import BinaryConverter 
from modules.Tree import Tree 
from modules.Tree_visualizer import TreeVisualizer
from modules.Json_exporter import JsonExporter 
from tkinter import Tk, filedialog

def main_ecripting(a,key):
    
    # Passo 1: Ler o arquivo de texto e converter para uma lista de caracteres
    input_text= ListStringConverter(a)
    char_list = input_text.convert()
    
    # Passo 2: Converter a lista de caracteres para seus valores ASCII decimais
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(char_list)
    
    
    # Passo 3: Realizar cálculos integrais simples nos valores ASCII
    obfuscador = IntegralProcessor()
    cripto = obfuscador.encrypt(ascii_values, key)
    
    # Passo 4: Converter os valores integrais para binário
    binary_converter = BinaryConverter()
    binary_values = binary_converter.float_bin_converter(cripto)
    
    
    # passo 5: Montar a árvore binária em pós ordem com os valores binários
    tree = Tree()
    tree.pos_order_insert(binary_values)
    visualizer = TreeVisualizer(tree)
    #visualizer.plot()
    values = tree.post_order_list()
    
    
    # passo 6: exportar a árvore em pós ordem para um arquivo txt em formato JSON
    exporter = JsonExporter(values,key)
    exporter.export_to_json('tree_output.txt')
    

def main_decripting(a, key):
    # passo 1: ler arquivo TXT com json
    input_text= ListStringConverter(a)
    char_list = input_text.convert_json()
    
    # passo 2: montar arvore binaria com valores do json
    tree = Tree()
    tree.pos_order_insert(char_list)
    visualizer = TreeVisualizer(tree)
    #visualizer.plot()
    values = tree.post_order_list()
    
    # passo 3: converter valores binarios para decimais
    binary_converter = BinaryConverter()
    binary_values = binary_converter.bin_float_converter(values)
    
    # passo 4: descazer integral
    obfuscador = IntegralProcessor()
    cripto = obfuscador.decrypt(binary_values, key)
    
    # passo 5: converter decimais para caracteres
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(cripto)
    
    # passo 6: tranformar lista de caracteres em texto e exportar em txt
    input_text.caracter_to_text(ascii_values,'descripto.txt')
    
    
# execução

if __name__ == "__main__":
    Tk().withdraw() 
    #caminho_origin = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Text files", "*.txt")])
    caminho_decript = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Text files", "*.txt")])
       
    entrada = input("Digite a chave privada: ")
    key = int(entrada)

    #main_ecripting(caminho_origin,key)
    main_decripting(caminho_decript, key)
