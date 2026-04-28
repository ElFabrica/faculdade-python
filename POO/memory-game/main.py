"""
=============================================================
  MODULE: main.py
  Ponto de entrada — gera assets e inicia o jogo
=============================================================
"""

import sys
import os

# Garante que o diretório do projeto está no path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Gera imagens se ainda não existem
from generate_assets import generate_all
from config import ASSETS_DIR

if not os.path.exists(os.path.join(ASSETS_DIR, "card_back.png")):
    print("Gerando assets das linguagens...")
    generate_all()

from modules.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
