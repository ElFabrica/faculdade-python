"""
=============================================================
  MODULE: modules/screens.py
  Telas do jogo: Menu, Inserir Nome, Game Over, Ranking
=============================================================
"""

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    COLOR_BG, COLOR_TEXT, COLOR_MUTED, COLOR_PRIMARY,
    COLOR_SECONDARY, COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER,
    COLOR_PANEL, COLOR_BORDER, COLOR_GOLD, COLOR_SILVER, COLOR_BRONZE,
)
from modules.ui import draw_text, draw_panel, Button, TextInput, get_font
from modules.ranking import RankingManager, RankingEntry


# ── Tela de Menu ─────────────────────────────────────────────
class MenuScreen:
    def __init__(self):
        cx = SCREEN_WIDTH // 2
        self.btn_play   = Button(cx - 120, 360, 240, 54, "▶  JOGAR",      COLOR_PRIMARY)
        self.btn_rank   = Button(cx - 120, 430, 240, 54, "🏆  RANKING",   COLOR_SECONDARY)
        self.btn_quit   = Button(cx - 120, 500, 240, 54, "✕  SAIR",       COLOR_DANGER)

    def handle_event(self, event) -> str | None:
        if self.btn_play.handle_event(event):  return "name_input"
        if self.btn_rank.handle_event(event):  return "ranking"
        if self.btn_quit.handle_event(event):  return "quit"
        return None

    def draw(self, surface):
        surface.fill(COLOR_BG)
        # Título
        draw_text(surface, "🧠 MEMORY GAME", SCREEN_WIDTH // 2, 140,
                  56, COLOR_PRIMARY, bold=True, anchor="center")
        draw_text(surface, "Linguagens de Programação", SCREEN_WIDTH // 2, 210,
                  22, COLOR_MUTED, anchor="center")

        # Decoração: lista de linguagens em arco
        langs = ["Python", "JS", "TS", "Rust", "Go", "Java", "C++", "Swift", "Kotlin"]
        for i, lang in enumerate(langs):
            x = 60 + i * 90
            y = 270 + (20 if i % 2 == 0 else 0)
            draw_text(surface, lang, x, y, 13, COLOR_MUTED, anchor="center")

        self.btn_play.draw(surface)
        self.btn_rank.draw(surface)
        self.btn_quit.draw(surface)

        draw_text(surface, "Encontre todos os pares de linguagens!", SCREEN_WIDTH // 2,
                  580, 15, COLOR_MUTED, anchor="center")


# ── Tela de Nome ─────────────────────────────────────────────
class NameInputScreen:
    def __init__(self):
        cx = SCREEN_WIDTH // 2
        self.input    = TextInput(cx - 180, 300, 360, 52, placeholder="Seu nome...", max_len=20)
        self.btn_start = Button(cx - 120, 390, 240, 50, "COMEÇAR →", COLOR_SUCCESS)
        self.btn_back  = Button(cx - 120, 458, 240, 44, "← Voltar", COLOR_PANEL)
        self.error_msg = ""

    def handle_event(self, event) -> str | None:
        self.input.handle_event(event)
        if self.btn_back.handle_event(event):  return "menu"
        if self.btn_start.handle_event(event) or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN
        ):
            if self.input.text.strip():
                return "game"
            self.error_msg = "Digite seu nome para continuar!"
        return None

    def update(self):
        self.input.update()

    def draw(self, surface):
        surface.fill(COLOR_BG)
        draw_text(surface, "Como você se chama?", SCREEN_WIDTH // 2, 200,
                  36, COLOR_TEXT, bold=True, anchor="center")
        draw_text(surface, "Seu nome aparecerá no ranking.", SCREEN_WIDTH // 2, 252,
                  18, COLOR_MUTED, anchor="center")
        self.input.draw(surface)
        self.btn_start.draw(surface)
        self.btn_back.draw(surface)
        if self.error_msg:
            draw_text(surface, self.error_msg, SCREEN_WIDTH // 2, 520,
                      16, COLOR_DANGER, anchor="center")


# ── Tela de Resultado ─────────────────────────────────────────
class ResultScreen:
    def __init__(self, player_name: str, score: int, pairs: int,
                 attempts: int, elapsed_str: str, position: int):
        self.player_name  = player_name
        self.score        = score
        self.pairs        = pairs
        self.attempts     = attempts
        self.elapsed_str  = elapsed_str
        self.position     = position
        errors            = max(0, attempts - pairs)
        accuracy          = round(pairs / attempts * 100, 1) if attempts else 0

        self.accuracy     = accuracy
        self.errors       = errors

        cx = SCREEN_WIDTH // 2
        self.btn_play   = Button(cx - 250, 560, 220, 50, "▶ Jogar Novamente", COLOR_PRIMARY)
        self.btn_rank   = Button(cx + 30,  560, 220, 50, "🏆 Ver Ranking",    COLOR_SECONDARY)

    def handle_event(self, event) -> str | None:
        if self.btn_play.handle_event(event): return "game"
        if self.btn_rank.handle_event(event): return "ranking"
        return None

    def draw(self, surface):
        surface.fill(COLOR_BG)

        # Painel central
        panel = pygame.Rect(SCREEN_WIDTH // 2 - 280, 80, 560, 460)
        draw_panel(surface, panel)

        medal = "🥇" if self.position == 1 else ("🥈" if self.position == 2 else
                ("🥉" if self.position == 3 else ""))
        draw_text(surface, f"Fim de jogo! {medal}", SCREEN_WIDTH // 2, 115,
                  34, COLOR_TEXT, bold=True, anchor="center")
        draw_text(surface, self.player_name, SCREEN_WIDTH // 2, 158,
                  22, COLOR_PRIMARY, anchor="center")

        # Pontuação grande
        score_color = COLOR_GOLD if self.position <= 3 else COLOR_SUCCESS
        draw_text(surface, str(self.score), SCREEN_WIDTH // 2, 210,
                  64, score_color, bold=True, anchor="center")
        draw_text(surface, "pontos", SCREEN_WIDTH // 2, 278,
                  18, COLOR_MUTED, anchor="center")

        # Stats
        stats = [
            ("Pares encontrados", f"{self.pairs} / 12"),
            ("Tentativas",        str(self.attempts)),
            ("Erros",             str(self.errors)),
            ("Precisão",          f"{self.accuracy}%"),
            ("Tempo",             self.elapsed_str),
            ("Posição no ranking", f"#{self.position}"),
        ]
        for i, (label, value) in enumerate(stats):
            col  = i % 2
            row  = i // 2
            x    = SCREEN_WIDTH // 2 - 220 + col * 250
            y    = 320 + row * 55
            draw_text(surface, label, x, y, 14, COLOR_MUTED)
            draw_text(surface, value, x, y + 20, 20, COLOR_TEXT, bold=True)

        self.btn_play.draw(surface)
        self.btn_rank.draw(surface)


# ── Tela de Ranking ───────────────────────────────────────────
class RankingScreen:
    def __init__(self, ranking_manager: RankingManager):
        self.entries = ranking_manager.load()[:15]
        cx = SCREEN_WIDTH // 2
        self.btn_back = Button(cx - 100, 636, 200, 44, "← Voltar", COLOR_PANEL)
        self._scroll  = 0

    def handle_event(self, event) -> str | None:
        if self.btn_back.handle_event(event): return "menu"
        return None

    def draw(self, surface):
        surface.fill(COLOR_BG)
        draw_text(surface, "🏆 RANKING", SCREEN_WIDTH // 2, 30,
                  38, COLOR_WARNING, bold=True, anchor="center")
        draw_text(surface, "Top 15 jogadores", SCREEN_WIDTH // 2, 78,
                  16, COLOR_MUTED, anchor="center")

        # Cabeçalho
        header_y = 110
        cols = [("#",55), ("Nome",200), ("Pontos",130), ("Precisão",110), ("Tempo",90), ("Data",140)]
        x = 30
        for label, width in cols:
            draw_text(surface, label, x, header_y, 14, COLOR_MUTED, bold=True)
            x += width

        pygame.draw.line(surface, COLOR_BORDER, (25, header_y + 22), (SCREEN_WIDTH - 25, header_y + 22))

        if not self.entries:
            draw_text(surface, "Nenhuma partida registrada ainda.", SCREEN_WIDTH // 2, 300,
                      20, COLOR_MUTED, anchor="center")
        else:
            for i, entry in enumerate(self.entries):
                y = 140 + i * 32
                if i == 0:   medal_color = COLOR_GOLD
                elif i == 1: medal_color = COLOR_SILVER
                elif i == 2: medal_color = COLOR_BRONZE
                else:        medal_color = COLOR_MUTED

                # Linha alternada
                if i % 2 == 0:
                    row_rect = pygame.Rect(25, y - 4, SCREEN_WIDTH - 50, 28)
                    pygame.draw.rect(surface, COLOR_PANEL, row_rect, border_radius=4)

                x = 30
                draw_text(surface, str(i + 1), x, y, 15, medal_color, bold=(i < 3))
                x += 55
                draw_text(surface, entry.name[:18], x, y, 15, COLOR_TEXT)
                x += 200
                draw_text(surface, str(entry.score), x, y, 15, medal_color if i < 3 else COLOR_TEXT, bold=(i < 3))
                x += 130
                draw_text(surface, f"{entry.accuracy}%", x, y, 15, COLOR_TEXT)
                x += 110
                draw_text(surface, entry.elapsed_str, x, y, 15, COLOR_TEXT)
                x += 90
                draw_text(surface, entry.date, x, y, 13, COLOR_MUTED)

        self.btn_back.draw(surface)
