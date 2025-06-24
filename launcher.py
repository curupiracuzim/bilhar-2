import os
import sys
import subprocess

# Caminho do script do jogo
script = 'em movimento sinuca.py'

# Garante que está no diretório do launcher
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Usa o mesmo Python que rodou o launcher
python_exe = sys.executable

try:
    subprocess.run([python_exe, script], check=True)
except Exception as e:
    print(f'Erro ao iniciar o jogo: {e}')
    input('Pressione Enter para sair...')
