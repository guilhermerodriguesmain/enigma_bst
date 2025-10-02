# Enigma project main module

# Este módulo integra vários módulos de processamento para demonstrar sua funcionalidade.

# Importa os módulos necessários
from modules.input_text import ListStringConverter 
from modules.ascii_converter import AsciiConverter 
from modules.PolySum_obfuscador import LogExpObfuscator
from modules.binary_converter import BinaryConverter 
from modules.Tree import Tree 
from modules.json_exporter import JsonExporter 
from tkinter import Tk, filedialog

def main_ecripting(a,b):
    
    # Passo 1: Ler o arquivo de texto e converter para uma lista de caracteres
    input_text= ListStringConverter(a)
    char_list = input_text.convert()
    
    # Passo 2: Converter a lista de caracteres para seus valores ASCII decimais
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(char_list)
    
    
    # Passo 3: Realizar cálculos integrais simples nos valores ASCII
    obfuscador = LogExpObfuscator(b)
    cripto = obfuscador.encrypt(ascii_values)
    
    # Passo 4: Converter os valores integrais para binário
    binary_converter = BinaryConverter()
    binary_values = binary_converter.encrypt(cripto)
    
    
    # passo 5: Montar a árvore binária em pós ordem com os valores binários
    tree = Tree()
    tree.Pos_order_insert(binary_values)
    values = tree.post_order_crypto()
    print("Valores em pós ordem:", values)
    
    
    # passo 6: exportar a árvore em pós ordem para um arquivo txt em formato JSON
    exporter = JsonExporter(values)
    exporter.export_to_json('tree_output.txt')
    
def main_decripting(a):
    
    # Passo 1: Ler o arquivo txt com a árvore em pós ordem em formato JSON e montar a árvore binária
    input_text= ListStringConverter(a)
    list_values = input_text.convert_json()
    
    # Passo 2: Percorrer a árvore em pós ordem e salvar os valores em uma lista
    tree = Tree()
    tree.Pos_order_insert(list_values)
    values = tree.post_order_crypto()
    print("Valores em pós ordem:", values)

    # Passo 3: Converter os valores binários para decimais
    binary_converter = BinaryConverter()
    decimal_values = binary_converter.decrypt(values)

    # Passo 4: Realizar o processo inverso dos cálculos integrais para obter os valores ASCII originais
    obfuscador = LogExpObfuscator(5) # chave 0 para descriptografar
    values = obfuscador.decrypt(decimal_values)
    
    # Passo 5: Converter os valores ASCII de volta para caracteres
    ascii_converter = AsciiConverter()
    char_list = ascii_converter.convert_multiple_from_ascii(values)
    
    # Passo 6: Juntar a lista de caracteres em uma string e salvar em um arquivo de texto
    input_text.caracter_to_text(char_list, 'decrypted_output.txt')

    pass
# execução

if __name__ == "__main__":
    Tk().withdraw() 
    caminho = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Text files", "*.txt")])
        
    entrada = input("Digite a chave de criptografia (separe por vírgula): ")
    key = int(entrada)

    main_ecripting(caminho,key)

    main_decripting('D:\\FACULDADE\\Periodos\\quarto_periodo\\EDA\\tree_output.txt',)
# main_decripting('tree_output.txt')