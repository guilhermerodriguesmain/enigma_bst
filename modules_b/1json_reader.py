#!/usr/bin/env python3
"""

Recebe JSON via:
 - arquivo (--file / -f)
 - string (--text / -t)
 - stdin (pipe)

 Como usar: arquivo, arraste ou crie arquivo com o arquivo JSON para o mesmo diretório, dentro dele coloque
  a mensagem JSON, abrindo terminal coloque python3 receive_json.py --file (nome do arquivo)

  mensagem: indo no terminal coloque, python3 receive_json.py --text (mensagem JSON) obs: linux, mac, cmd
  podem ter meios diferentes de escrever o arquivo JSON

  stdin: echo, indo no terminal escreva "echo '{ "nome": "João", "idade": 30 }' | python3 receive_json.py"
  cat, indo no terminal escreva cat (arquivo com o JSON) | python3 receive_json.py
"""

import sys
import argparse
import json
from typing import Any

# ---------- Leitura ----------

def carregar_de_arquivo(caminho: str) -> str:
    """
       Função responsável por carregar o conteúdo de um arquivo de texto.
       - Tenta abrir com codificação UTF-8.
       - Se falhar (erro de decodificação), faz fallback para Latin-1.
       Retorna o conteúdo como string.
    """
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # fallback razoável para arquivos que não estão em UTF-8
        with open(caminho, 'r', encoding='latin-1') as f:
            return f.read()

def carregar_de_stdin() -> str:
    """
        Lê toda a entrada padrão (stdin).
        Útil para quando o programa recebe dados via pipe no terminal.
    """
    return sys.stdin.read()


def mostrar_erro_json(e: json.JSONDecodeError, texto: str, contexto: int = 40) -> None:
    """
        Exibe mensagens de erro detalhadas quando o JSON não pode ser decodificado.
        - Mostra a mensagem de erro.
        - Exibe um trecho do texto ao redor da posição onde ocorreu o erro.
        - Marca a posição exata com um '^'.
        Isso ajuda a depurar problemas em strings JSON inválidas.
    """
    pos = e.pos if hasattr(e, 'pos') else None
    print(f"Erro ao decodificar JSON: {e.msg}", file=sys.stderr)
    if pos is not None:
        start = max(0, pos - contexto)
        end = min(len(texto), pos + contexto)
        snippet = texto[start:end].replace('\n', '\\n')
        pointer = ' ' * (min(pos, contexto)) + '^'
        print(f"\nContexto (posição {pos}):\n...{snippet}...", file=sys.stderr)
        print(f"{' ' * 3}{pointer}\n", file=sys.stderr)
    else:
        print(str(e), file=sys.stderr)

def imprimir_json_formatado(obj: Any, caminho: str = "") -> None:
    """
        Percorre recursivamente o objeto JSON e imprime em formato legível.
        - Para dicionários: imprime as chaves e valores.
        - Para listas:
            - Se forem valores simples (str, int, float, bool, None), mostra todos na mesma linha.
            - Se forem dicionários, tenta gerar resumos (tipo, cidade/UF, nome, nível).
            - Se forem mistos, percorre item a item recursivamente.
        - Para valores simples: imprime diretamente.
        Esse método gera uma saída mais organizada e fácil de interpretar.
        """


    "Saida do Json formatado"
    if isinstance(obj, dict):
        for chave, valor in obj.items():
            nova_chave = f"{caminho}.{chave}" if caminho else chave
            imprimir_json_formatado(valor, nova_chave)

    elif isinstance(obj, list):
        # Lista de valores simples
        if all(isinstance(item, (str, int, float, bool, type(None))) for item in obj):
            valores = ', '.join(str(item) for item in obj)
            print(f"{caminho}: {valores}")

        # Lista de dicionários
        elif all(isinstance(item, dict) for item in obj):
            # Tenta gerar uma string resumo por item
            resumos = []
            for item in obj:
                if 'tipo' in item:
                    partes = []
                    partes.append(item['tipo'])
                    if 'cidade' in item and 'uf' in item:
                        partes.append(f"{item['cidade']}/{item['uf']}")
                    elif 'cidade' in item:
                        partes.append(item['cidade'])
                    elif 'uf' in item:
                        partes.append(item['uf'])
                    resumo = ' - '.join(partes)
                    resumos.append(resumo)
                elif 'nome' in item and 'nivel' in item:
                    resumos.append(f"{item['nome']} ({item['nivel']})")
                else:
                    valores = ' '.join(str(v) for v in item.values())
                    resumos.append(valores)
            print(f"{caminho}: {', '.join(resumos)}")

        else:
            # Lista mista ou desconhecida
            for i, item in enumerate(obj):
                nova_chave = f"{caminho}[{i}]"
                imprimir_json_formatado(item, nova_chave)

    else:
        print(f"{caminho}: {obj}")

# ---------- Fluxo principal ----------

def main() -> None:
    """
        Função principal do programa.
        - Configura os argumentos de linha de comando (argparse).
        - Permite entrada de JSON via:
            --file (arquivo),
            --text (string),
            stdin (pipe).
        - Valida e carrega o JSON.
        - Se válido:
            - Exibe formatado com indentação (se --raw).
            - Ou mostra saída personalizada (imprimir_json_formatado).
        - Se inválido: mostra mensagem de erro detalhada.
        """


    p = argparse.ArgumentParser(
        description="Valida e formata uma string JSON (arquivo / texto / stdin)."
    )
    group = p.add_mutually_exclusive_group()
    group.add_argument("--file", "-f", help="Caminho para arquivo contendo JSON")
    group.add_argument("--text", "-t", help='Uma string com JSON (ex: \'{"a":1}\')')
    p.add_argument("--raw", action="store_true", help="Exibir JSON com indentação padrão (json.dumps)")
    args = p.parse_args()

    # obter conteúdo
    if args.file:
        try:
            conteudo = carregar_de_arquivo(args.file)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {args.file}", file=sys.stderr)
            sys.exit(2)
        except PermissionError:
            print(f"Permissão negada ao abrir: {args.file}", file=sys.stderr)
            sys.exit(2)
        except Exception as e:
            print(f"Erro ao ler arquivo {args.file}: {e}", file=sys.stderr)
            sys.exit(2)
    elif args.text:
        conteudo = args.text
    else:
        if sys.stdin.isatty():
            print("Nenhuma entrada fornecida. Use --file, --text ou passe via stdin.", file=sys.stderr)
            p.print_help()
            sys.exit(1)
        conteudo = carregar_de_stdin()

    conteudo = conteudo.strip()
    if not conteudo:
        print("Entrada vazia.", file=sys.stderr)
        sys.exit(1)


    try:
        obj = json.loads(conteudo)
    except json.JSONDecodeError as e:
        mostrar_erro_json(e, conteudo)
        sys.exit(1)
    except Exception as e:

        print(f"Erro inesperado ao tentar carregar JSON: {e}", file=sys.stderr)
        sys.exit(1)


    if args.raw:
        print(json.dumps(obj, ensure_ascii=False, indent=2))
    else:
        imprimir_json_formatado(obj)

    sys.exit(0)

if __name__ == "__main__":
    main()
