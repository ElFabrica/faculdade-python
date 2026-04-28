"""
=============================================================
  MODULE: modules/game.py
  Classe Game — máquina de estados e loop principal do jogo
=============================================================
"""

import sys
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, COLOR_BG
from modules.board   import Board
from modules.player  import Player
from modules.ranking import RankingManager
from modules.hud     import HUD
from modules.screens import (
    MenuScreen, NameInputScreen, ResultScreen, RankingScreen
)


class Game:
    """Controlador principal — gerencia estados e o loop de jogo."""

    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock   = pygame.time.Clock()

        self.ranking_manager = RankingManager()
        self.board           = Board()
        self.board.load_images()

        self.player: Player | None = None
        self._state = "menu"

        # Instâncias de tela
        self._menu_screen:   MenuScreen       = MenuScreen()
        self._name_screen:   NameInputScreen  = NameInputScreen()
        self._result_screen: ResultScreen | None = None
        self._rank_screen:   RankingScreen | None = None
        self._hud:           HUD              = HUD()

    # ── Loop principal ───────────────────────────────────────
    def run(self):
        while True:
            dt = self.clock.tick(FPS)
            self._handle_events()
            self._update(dt)
            self._draw()
            pygame.display.flip()

    # ── Troca de estado ──────────────────────────────────────
    def _transition(self, next_state: str):
        if next_state == "quit":
            pygame.quit()
            sys.exit()

        if next_state == "game":
            name = self._name_screen.input.text.strip() or "Anônimo"
            self.player = Player(name)
            self.board.setup()
            self.player.start_timer()

        if next_state == "ranking":
            self._rank_screen = RankingScreen(self.ranking_manager)

        if next_state == "menu":
            self._menu_screen  = MenuScreen()

        if next_state == "name_input":
            self._name_screen = NameInputScreen()

        self._state = next_state

    def _finish_game(self):
        self.player.stop_timer()
        score = self.player.compute_score(
            self.board.pairs_found,
            self.board.total_attempts,
            self.player.elapsed_seconds,
        )
        self.ranking_manager.save_entry(
            name     = self.player.name,
            score    = score,
            pairs    = self.board.pairs_found,
            attempts = self.board.total_attempts,
            elapsed  = self.player.elapsed_seconds,
        )
        position = self.ranking_manager.get_position(score)
        self._result_screen = ResultScreen(
            player_name  = self.player.name,
            score        = score,
            pairs        = self.board.pairs_found,
            attempts     = self.board.total_attempts,
            elapsed_str  = self.player.elapsed_str,
            position     = position,
        )
        self._state = "result"

    # ── Eventos ──────────────────────────────────────────────
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            next_state = None

            if self._state == "menu":
                next_state = self._menu_screen.handle_event(event)

            elif self._state == "name_input":
                next_state = self._name_screen.handle_event(event)

            elif self._state == "game":
                if self._hud.handle_event(event):
                    next_state = "menu"
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.board.handle_click(event.pos)

            elif self._state == "result":
                next_state = self._result_screen.handle_event(event)

            elif self._state == "ranking":
                next_state = self._rank_screen.handle_event(event)

            if next_state:
                self._transition(next_state)

    # ── Update ───────────────────────────────────────────────
    def _update(self, dt: int):
        if self._state == "name_input":
            self._name_screen.update()

        elif self._state == "game":
            self.board.update(dt)
            if self.board.is_complete:
                self._finish_game()

    # ── Draw ─────────────────────────────────────────────────
    def _draw(self):
        self.screen.fill(COLOR_BG)

        if self._state == "menu":
            self._menu_screen.draw(self.screen)

        elif self._state == "name_input":
            self._name_screen.draw(self.screen)

        elif self._state == "game":
            self._hud.draw(
                self.screen,
                self.player.name,
                self.board.pairs_found,
                self.board.total_pairs,
                self.board.total_attempts,
                self.player.elapsed_str,
            )
            self.board.draw(self.screen)

        elif self._state == "result":
            self._result_screen.draw(self.screen)

        elif self._state == "ranking":
            self._rank_screen.draw(self.screen)
