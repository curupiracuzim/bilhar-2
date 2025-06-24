import os
import subprocess
import sys

def main():
    # Caminho do jogo
    pasta = os.path.dirname(os.path.abspath(__file__))
    jogo = os.path.join(pasta, "em movimento sinuca.py")
    if not os.path.exists(jogo):
        # Tenta launcher.py se existir
        jogo = os.path.join(pasta, "launcher.py")
    if not os.path.exists(jogo):
        print("Jogo não encontrado!")
        return

    # Executa o jogo com o Python padrão do sistema
    try:
        subprocess.Popen([sys.executable, jogo], cwd=pasta)
    except Exception as e:
        print("Erro ao iniciar o jogo:", e)

if __name__ == "__main__":
    main()
