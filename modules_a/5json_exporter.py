class CodigoBinario:
    def __init__(self, codigo_embaralhado: str):
        self.codigo = codigo_embaralhado

    def salvar_em_arquivo(self, nome_arquivo="codigo_embaralhado.txt"):
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(self.codigo)
        print(f"Código salvo em '{nome_arquivo}'")

class Aplicacao:
    def __init__(self):
        # Simula o recebimento do código binário embaralhado - quando importar os outros modulos, colcoar a variavel que
        # guarda o código binario embaralhado aqui
        codigo_embaralhado = "1010101110010110101011100010101"
        self.codigo_binario = CodigoBinario(codigo_embaralhado)

    def run(self):
        self.codigo_binario.salvar_em_arquivo()

if __name__ == "__main__":
    app = Aplicacao()
    app.run()
