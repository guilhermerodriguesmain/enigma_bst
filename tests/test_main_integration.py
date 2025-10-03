# tests/test_main_integration.py

import pytest
from pathlib import Path

# Importa as funções principais do seu script corrigido
from main import main_ecripting, main_decripting

def test_full_cycle_with_corrected_logic(tmp_path, monkeypatch, mocker):
    """
    Testa o ciclo completo de criptografia e descriptografia com a lógica
    corrigida, esperando que o texto original seja recuperado perfeitamente.
    """
    # 1. ARRANGE (Preparação)

    # Mock de componentes de interface com o usuário e sistema
    mocker.patch('main.TreeVisualizer.plot', return_value=None)
    mocker.patch('builtins.input', return_value='final_output') # Simula o usuário digitando o nome do arquivo de saída
    
    # Muda o diretório de trabalho para uma pasta temporária
    monkeypatch.chdir(tmp_path)
    
    # Cria o arquivo de texto inicial
    original_text = "abc"
    input_file = Path("start.txt")
    input_file.write_text(original_text)
    
    # Define os nomes dos arquivos que serão criados durante o processo
    intermediate_file = Path("tree_output.json")
    final_output_file = Path("final_output.txt")

    # 2. ACT (Execução)
    
    # Executa o processo de criptografia com a chave correta
    main_ecripting(str(input_file))
    
    # Executa o processo de descriptografia
    main_decripting(str(intermediate_file))

    # 3. ASSERT (Verificação)

    # Garante que os arquivos esperados foram criados
    assert intermediate_file.exists(), "O arquivo JSON intermediário não foi criado."
    assert final_output_file.exists(), "O arquivo de saída final não foi criado."
    
    # Lê o conteúdo do arquivo final gerado
    decrypted_text = final_output_file.read_text()
    
    # VERIFICAÇÃO PRINCIPAL:
    # Com o código corrigido, o texto descriptografado deve ser
    # idêntico ao texto original.
    assert decrypted_text == original_text