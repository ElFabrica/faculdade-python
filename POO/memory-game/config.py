"""
=============================================================
  MODULE: config.py
  Configurações globais do jogo — cores, dimensões, caminhos
=============================================================
"""

import os

# ── Diretórios base ──────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR  = os.path.join(BASE_DIR, "assets", "images")
DATA_DIR    = os.path.join(BASE_DIR, "data")
RANKING_FILE = os.path.join(DATA_DIR, "ranking.txt")

# ── Janela ───────────────────────────────────────────────────
SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 700
FPS           = 60
TITLE         = "Memory Game — Linguagens de Programação"

# ── Tabuleiro ────────────────────────────────────────────────
CARD_WIDTH    = 110
CARD_HEIGHT   = 110
CARD_MARGIN   = 12
BOARD_COLS    = 6
BOARD_ROWS    = 4
BOARD_OFFSET_X = 45
BOARD_OFFSET_Y = 130

# ── Tempo ────────────────────────────────────────────────────
FLIP_DELAY_MS    = 900
FLIP_ANIM_STEPS  = 8

# ── Cores ────────────────────────────────────────────────────
COLOR_BG         = (15, 15, 35)
COLOR_PRIMARY    = (99, 102, 241)
COLOR_SECONDARY  = (236, 72, 153)
COLOR_SUCCESS    = (34, 197, 94)
COLOR_WARNING    = (251, 191, 36)
COLOR_DANGER     = (239, 68, 68)
COLOR_TEXT       = (241, 245, 249)
COLOR_MUTED      = (100, 116, 139)
COLOR_CARD_BG    = (30, 41, 59)
COLOR_PANEL      = (22, 28, 48)
COLOR_BORDER     = (51, 65, 85)
COLOR_GOLD       = (255, 215, 0)
COLOR_SILVER     = (192, 192, 192)
COLOR_BRONZE     = (205, 127, 50)

# ── Linguagens disponíveis para o jogo ───────────────────────
LANGUAGES = [
    "Python", "JavaScript", "TypeScript", "Rust",
    "Go", "Java", "C++", "Swift",
    "Kotlin", "Ruby", "PHP", "Dart",
]
