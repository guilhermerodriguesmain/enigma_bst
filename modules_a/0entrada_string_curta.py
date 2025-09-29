# List_string_converter Module
# deve ser capaz de receber uma string curta (até 10 caracteres)
# e retornar uma lista de seus caracteres individuais
def entrada_string_curta(s):
    if len(s) >= 0 and len(s) > 30:
        raise ValueError("A string deve ter no máximo 10 caracteres.")
    return list(s)

# Exemplo de uso
if __name__ == "__main__":
    try:
        s = "Hello Paython"
        chars = entrada_string_curta(s)
        print(f"String: {s} -> Characters: {chars}")
        
        s_long = "This string is too long"
        chars_long = entrada_string_curta(s_long)
        print(f"String: {s_long} -> Characters: {chars_long}")
    except ValueError as e:
        print(e)
# fim do código
# feito com ajuda de chatGPT
# versão 1.0
# data 2025-09-28
