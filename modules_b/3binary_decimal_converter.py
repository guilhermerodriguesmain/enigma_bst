from typing import Any


'''
    Como usar: Após o main defina uma variavel com numeros binarios, exemplo:
    ''s1 = "1101 1010 1111"
    print("Teste string:", s1)
    print("Decimal:", descriptografar_binario(s1))'' após isso só dar um play q ele converte para numeros decimais  
'''

def descriptografar_binario(bin_str: str) -> Any:
    """
    Recebe uma string binária (pode ter espaços, linhas ou ser contínua)
    e retorna os valores decimais correspondentes.
    Agora trata os binários como números puros (não ASCII).
    """
    try:
        bin_str = bin_str.strip().replace('\n', ' ').replace('\r', ' ')
        partes = bin_str.split()

        # Se só tem um bloco contínuo, mantém assim
        if len(partes) == 1 and all(c in '01' for c in partes[0]):
            partes = [partes[0]]

        # Converte todos os binários válidos
        decimais = [int(b, 2) for b in partes if all(c in '01' for c in b)]

        return decimais if len(decimais) > 1 else decimais[0]
    except Exception:
        return bin_str  # se falhar, retorna original

def decodificar_json(dado: Any) -> Any:
    """
    Percorre recursivamente o JSON e descriptografa strings binárias.
    """
    if isinstance(dado, str):
        return descriptografar_binario(dado)
    elif isinstance(dado, list):
        return [decodificar_json(item) for item in dado]
    elif isinstance(dado, dict):
        return {k: decodificar_json(v) for k, v in dado.items()}
    else:
        return dado

# Testes simples
if __name__ == "__main__":
    # Exemplo com lista de strings binárias
    l1 = ["1101", "1010", "1111"]
    print("\nTeste lista:", l1)
    print("Decimal:", decodificar_json(l1))

