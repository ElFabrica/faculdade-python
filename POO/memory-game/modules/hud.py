"""
=============================================================
  MODULE: modules/hud.py
  HUD — painel superior com informações durante o jogo
=============================================================
"""

import pygame
from config import (
    SCREEN_WIDTH, COLOR_PANEL, COLOR_BORDER,
    COLOR_TEXT, COLOR_MUTED, COLOR_SUCCESS, COLOR_WARNING,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DANGER
)
from modules.ui import draw_text, draw_panel, Button, get_font


class HUD:
    def __init__(self):
        self.btn_menu = Button(SCREEN_WIDTH - 130, 18, 110, 38,
                               "← Menu", color=COLOR_PANEL, font_size=15)

    def draw(self, surface: pygame.Surface, player_name: str,
             pairs: int, total_pairs: int, attempts: int, elapsed_str: str):

        # Painel HUD
        panel = pygame.Rect(0, 0, SCREEN_WIDTH, 108)
        draw_panel(surface, panel, color=COLOR_PANEL, radius=0)
        pygame.draw.line(surface, COLOR_BORDER, (0, 108), (SCREEN_WIDTH, 108))

        # Jogador
        draw_text(surface, "Jogador", 20, 12, 13, COLOR_MUTED)
        draw_text(surface, player_name, 20, 30, 20, COLOR_TEXT, bold=True)

        # Pares
        draw_text(surface, "Pares", 200, 12, 13, COLOR_MUTED)
        draw_text(surface, f"{pairs} / {total_pairs}", 200, 30, 22, COLOR_SUCCESS, bold=True)

        # Tentativas
        draw_text(surface, "Tentativas", 340, 12, 13, COLOR_MUTED)
        draw_text(surface, str(attempts), 340, 30, 22, COLOR_WARNING, bold=True)

        # Precisão
        accuracy = round(pairs / attempts * 100, 1) if attempts else 0.0
        acc_color = COLOR_SUCCESS if accuracy >= 70 else (COLOR_WARNING if accuracy >= 40 else COLOR_DANGER)
        draw_text(surface, "Precisão", 470, 12, 13, COLOR_MUTED)
        draw_text(surface, f"{accuracy}%", 470, 30, 22, acc_color, bold=True)

        # Tempo
        draw_text(surface, "Tempo", 610, 12, 13, COLOR_MUTED)
        draw_text(surface, elapsed_str, 610, 30, 22, COLOR_PRIMARY, bold=True)

        # Barra de progresso
        bar_rect = pygame.Rect(20, 72, SCREEN_WIDTH - 160, 16)
        pygame.draw.rect(surface, COLOR_BORDER, bar_rect, border_radius=8)
        progress = pairs / total_pairs if total_pairs else 0
        if progress > 0:
            fill_w = int(bar_rect.width * progress)
            fill_rect = pygame.Rect(bar_rect.x, bar_rect.y, fill_w, bar_rect.height)
            pygame.draw.rect(surface, COLOR_SUCCESS, fill_rect, border_radius=8)
        draw_text(surface, f"{int(progress * 100)}%", bar_rect.right + 10, 72, 13, COLOR_MUTED)

        self.btn_menu.draw(surface)

    def handle_event(self, event) -> bool:
        return self.btn_menu.handle_event(event)
