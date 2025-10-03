# Enigma project main module

# Este módulo integra vários módulos de processamento para demonstrar sua funcionalidade.

# Importa os módulos necessários
from modules.input_text import ListStringConverter 
from modules.ascii_converter import AsciiConverter 
from modules.IntegralProcessor import IntegralProcessor
from modules.binary_converter import BinaryConverter 
from modules.Tree import Tree 
from modules.Tree_visualizer import TreeVisualizer
from modules.json_exporter import JsonExporter 
from tkinter import Tk, filedialog

def main_ecripting(a):
    pub_key=0
    private_key = pub_key**2
    # Passo 1: Ler o arquivo de texto e converter para uma lista de caracteres
    input_text= ListStringConverter(a)
    char_list = input_text.convert() # retorna publickey, charlist
    pub_key=len(char_list)
    # Passo 2: Converter a lista de caracteres para seus valores ASCII decimais
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(char_list)
    
    
    # Passo 3: Realizar cálculos integrais simples nos valores ASCII
    obfuscador = IntegralProcessor()
    cripto = obfuscador.encrypt(ascii_values, private_key)
    
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
    exporter = JsonExporter(values,pub_key)
    exporter.export_to_json('tree_output.txt')
    
    

def main_decripting(a):
    
    """private key = public key **2 """
    # passo 1: ler arquivo TXT com json
    input_text= ListStringConverter(a)
    char_list = input_text.convert_json()
    private_key = char_list[0]**2
    # passo 2: montar arvore binaria com valores do json
    tree = Tree()
    tree.pos_order_insert(char_list[1])
    visualizer = TreeVisualizer(tree)
    #visualizer.plot()
    values = tree.post_order_list()
    
    # passo 3: converter valores binarios para decimais
    binary_converter = BinaryConverter()
    binary_values = binary_converter.bin_float_converter(values)
    
    # passo 4: descazer integral
    obfuscador = IntegralProcessor()
    cripto = obfuscador.decrypt(binary_values, private_key)
    
    # passo 5: converter decimais para caracteres
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(cripto)
    
    # passo 6: tranformar lista de caracteres em texto e exportar em txt
    file_name = input("digite o nome desejado para o arquivo: ")
    input_text.caracter_to_text(ascii_values,file_name)
    
    
# execução

if __name__ == "__main__":
    
    while True:
        menu = """
        1940 — Ordem de um irmão de armas

O ano é 1940. Você é um soldado alemão, isolado na trincheira, com a lama até os joelhos e o estalo distante de tiros ao longe. Na sua frente, repousa a máquina Enigma, pequena, complexa, mortal em sua precisão. Ela é a chave para proteger a vida de seus aliados e a execução de ordens vitais.

Hoje, você tem uma missão crítica: receber ou enviar mensagens criptografadas. Não é o inimigo que fala aqui — é um aliado, alguém que confia em você para interpretar suas palavras e agir corretamente. Cada caractere decifrado ou codificado pode salvar vidas, redirecionar tropas ou garantir o sucesso da missão.

--------- MENU ---------
1 → Encriptar e enviar uma mensagem para um aliado via Enigma
2 → Receber e descriptografar uma mensagem de um aliado via Enigma
0 → Desistir e voltar para a lama

Escolha com cuidado. A máquina não erra, mas você sim.
        """
        print(menu)
        decisao = int(input("\n\nQual vai ser sua escolha ? \nDIGITE AQUI:"))
        
        if decisao == 1:
            Tk().withdraw() 
            caminho_origin = filedialog.askopenfilename(title="Selecione o arquivo TXT para criptografar", filetypes=[("Text files", "*.txt")])
            
            entrada = input("Digite a chave publica: ")
            key = int(entrada)

            main_ecripting(caminho_origin,key)
            
        elif decisao == 2:
            
#-----caminho_decript apresenta um bug de congelamento 
            caminho_decript = filedialog.askopenfilename(title="Selecione o arquivo TXT para descriptografar", filetypes=[("Text files", "*.txt")])

            entrada_2 = input("Digite a chave privada: ")
            key_2 = int(entrada_2)
            main_decripting(caminho_decript, key_2)
            
        elif decisao == 0 :
            print("Você foi fraco e preferiu a lama ")
            break
        
        else:
            print("Escolha entre os digitos disponiveis no menu")
        
