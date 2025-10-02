#!/usr/bin/env python3

import sys
import argparse
import json
from typing import Any, List, Union


class EntradaJSON:
    def __init__(self, args: argparse.Namespace):
        self.args = args

    def ler(self) -> str:
        if self.args.arquivo:
            return self._carregar_de_arquivo(self.args.arquivo)
        elif self.args.texto:
            return self.args.texto.strip()
        elif not sys.stdin.isatty():
            return self._carregar_de_stdin().strip()
        else:
            print("Nenhuma entrada fornecida. Use --arquivo/--file, --texto/--text ou passe via stdin.", file=sys.stderr)
            sys.exit(1)

    def _carregar_de_arquivo(self, caminho: str) -> str:
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            with open(caminho, 'r', encoding='latin-1') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {caminho}", file=sys.stderr)
            sys.exit(2)
        except PermissionError:
            print(f"Permissão negada ao abrir: {caminho}", file=sys.stderr)
            sys.exit(2)
        except Exception as e:
            print(f"Erro ao ler arquivo {caminho}: {e}", file=sys.stderr)
            sys.exit(2)

    def _carregar_de_stdin(self) -> str:
        return sys.stdin.read()


class ValidadorJSON:
    def __init__(self, texto: str):
        self.texto = texto

    def carregar(self) -> Any:
        try:
            return json.loads(self.texto)
        except json.JSONDecodeError as e:
            self._mostrar_erro_json(e)
            sys.exit(1)
        except Exception as e:
            print(f"Erro inesperado ao tentar carregar JSON: {e}", file=sys.stderr)
            sys.exit(1)

    def _mostrar_erro_json(self, e: json.JSONDecodeError, contexto: int = 40) -> None:
        pos = getattr(e, 'pos', None)
        print(f"Erro ao decodificar JSON: {e.msg}", file=sys.stderr)
        if pos is not None:
            start = max(0, pos - contexto)
            end = min(len(self.texto), pos + contexto)
            snippet = self.texto[start:end].replace('\n', '\\n')
            pointer = ' ' * (min(pos, contexto)) + '^'
            print(f"\nContexto (posição {pos}):\n...{snippet}...", file=sys.stderr)
            print(f"{' ' * 3}{pointer}\n", file=sys.stderr)
        else:
            print(str(e), file=sys.stderr)


class TransformadorJSON:
    @staticmethod
    def para_lista_iteravel(obj: Any) -> List:
        if isinstance(obj, dict):
            return list(obj.items())
        elif isinstance(obj, list):
            return obj
        else:
            return [obj]


class FormatadorJSON:
    def __init__(self, obj: Any):
        self.obj = obj

    def imprimir(self, caminho: str = "") -> None:
        self._imprimir_formatado(self.obj, caminho)

    def _imprimir_formatado(self, obj: Any, caminho: str) -> None:
        if isinstance(obj, dict):
            for chave, valor in obj.items():
                nova_chave = f"{caminho}.{chave}" if caminho else chave
                self._imprimir_formatado(valor, nova_chave)
        elif isinstance(obj, list):
            if all(isinstance(item, (str, int, float, bool, type(None))) for item in obj):
                valores = ', '.join(str(item) for item in obj)
                print(f"{caminho}: {valores}")
            elif all(isinstance(item, dict) for item in obj):
                resumos = []
                for item in obj:
                    if 'tipo' in item:
                        partes = [item['tipo']]
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
                for i, item in enumerate(obj):
                    nova_chave = f"{caminho}[{i}]"
                    self._imprimir_formatado(item, nova_chave)
        else:
            print(f"{caminho}: {obj}")


class AplicativoJSON:
    def __init__(self):
        self.args = self._configurar_argumentos()

    def _configurar_argumentos(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description="Valida e formata uma string JSON (arquivo / texto / stdin).")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--arquivo", "--file", "-f", help="Caminho para arquivo contendo JSON")
        group.add_argument("--texto", "--text", "-t", help="Uma string com JSON (ex: '{\"a\":1}')")
        parser.add_argument("--cru", "--raw", action="store_true", help="Exibir JSON com indentação padrão (json.dumps)")
        return parser.parse_args()

    def executar(self) -> None:
        leitor = EntradaJSON(self.args)
        conteudo = leitor.ler()

        if not conteudo.strip():
            print("Entrada vazia.", file=sys.stderr)
            sys.exit(1)

        validador = ValidadorJSON(conteudo)
        obj = validador.carregar()

        lista = TransformadorJSON.para_lista_iteravel(obj)
        print("Lista Iterável:", lista)

        if self.args.cru:
            print(json.dumps(obj, ensure_ascii=False, indent=2))
        else:
            formatador = FormatadorJSON(obj)
            formatador.imprimir()

        sys.exit(0)


if __name__ == "__main__":
    app = AplicativoJSON()
    app.executar()
