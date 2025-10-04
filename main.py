# Enigma project main module

# Este módulo integra vários módulos de processamento para demonstrar sua funcionalidade.

# Importa os módulos necessários
from modules.input_text import ListStringConverter 
from modules.ascii_converter import AsciiConverter 
from modules.IntegralProcessor import IntegralProcessor
from modules.binary_converter import BinaryConverter 
from modules.Tree import Tree 
from modules.json_exporter import JsonExporter 
from tkinter import Tk, filedialog
import os

from dotenv import load_dotenv


# Carrega variáveis do .env
load_dotenv()

def main_ecripting(a):
    # Passo 1: Ler o arquivo de texto
    input_text = ListStringConverter(a)
    char_list = input_text.convert()
    
    # Passo 2: Definir as chaves APÓS ter a informação necessária
    pub_key = len(char_list)
    private_key = int(os.getenv("PRIVATE_KEY"))
    
    # Passo 3: Converter para ASCII
    ascii_converter = AsciiConverter()
    ascii_values = ascii_converter.convert_multiple_to_ascii(char_list)
    
    # Passo 4: Criptografar com a chave correta
    obfuscador = IntegralProcessor()
    cripto = obfuscador.encrypt(ascii_values, private_key)
    
    # Passo 5: Converter para binário
    binary_converter = BinaryConverter()
    binary_values = binary_converter.float_bin_converter(cripto)
    
    # Passo 6: Montar a árvore e imprimir no terminal
    tree = Tree()
    tree.pos_order_insert(binary_values)
    tree.print_tree()
    values = tree.post_order_list()
    
    # Passo 7: Exportar para JSON
    exporter = JsonExporter(values, pub_key)
    exporter.export_to_json('tree_output.json')
    
def main_decripting(a):
    # Passo 1: Ler o JSON
    input_text = ListStringConverter(a)
    # SUGESTÃO: Renomear variável para maior clareza
    pub_key, tree_values = input_text.convert_json()
    
    # Passo 2: Calcular a chave privada a partir da chave pública lida
    private_key = int(os.getenv("PRIVATE_KEY"))
    
    
    # Passo 3: Montar a árvore com os valores lidos
    tree = Tree()
    tree.pos_order_insert(tree_values)
    # A visualização da árvore no terminal
    tree.print_tree()
    values = tree.post_order_list()
    
    # Passo 4: Converter de binário para float
    binary_converter = BinaryConverter()
    binary_values = binary_converter.bin_float_converter(values)
    
    # Passo 5: Desfazer a integral para obter os códigos ASCII
    obfuscador = IntegralProcessor()
    cripto = obfuscador.decrypt(binary_values, private_key)
    
    # Passo 6: Converter os códigos ASCII de volta para caracteres
    ascii_converter = AsciiConverter()
    # Esta linha já estava correta no seu código, ótimo!
    final_chars = ascii_converter.convert_multiple_from_ascii(cripto)
    
    # Passo 7: Salvar o texto final em um arquivo
    file_name = input("Digite o nome desejado para o arquivo de saída: ")
    input_text.caracter_to_text(final_chars, file_name)

    
# ------------------------------   execução   ----------------------------------------------------

  
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    
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
        
            caminho_origin = filedialog.askopenfilename(
            title="Selecione o arquivo TXT para criptografar",
            filetypes=[("Text files", "*.txt")]
        )
            main_ecripting(caminho_origin)
            
        elif decisao == 2:
            
#--------------------------------------------------------------------caminho_decript 
  
            caminho_decript = filedialog.askopenfilename(
            title="Selecione o arquivo TXT para descriptografar",
            filetypes=[("Text files", "*.json")]
        )
            main_decripting(caminho_decript)
            
        elif decisao == 0 :
            print("Você foi fraco e preferiu a lama ")
            break
        
        else:
            print("Escolha entre os digitos disponiveis no menu")
        
