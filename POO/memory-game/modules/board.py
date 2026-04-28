"""
=============================================================
  MODULE: modules/board.py
  Classe Board — gerencia o tabuleiro, cartas e lógica de pares
=============================================================
"""

import os
import random
import pygame
from config import (
    CARD_WIDTH, CARD_HEIGHT, CARD_MARGIN,
    BOARD_COLS, BOARD_ROWS, BOARD_OFFSET_X, BOARD_OFFSET_Y,
    ASSETS_DIR, LANGUAGES, FLIP_DELAY_MS
)
from modules.card import Card


class Board:
    """Tabuleiro do jogo da memória."""

    def __init__(self):
        self.cards: list[Card] = []
        self._face_up: list[Card] = []   # Cartas abertas aguardando verificação
        self._wait_timer   = 0           # ms restando para fechar cartas erradas
        self._waiting      = False       # Se estamos no delay de erro
        self.pairs_found   = 0
        self.total_attempts = 0
        self._images: dict[str, pygame.Surface] = {}
        self._back_image: pygame.Surface | None = None

    # ── Inicialização ────────────────────────────────────────
    def load_images(self):
        """Carrega as imagens das linguagens do disco."""
        back_path = os.path.join(ASSETS_DIR, "card_back.png")
        self._back_image = pygame.image.load(back_path).convert_alpha()
        self._back_image = pygame.transform.scale(self._back_image, (CARD_WIDTH, CARD_HEIGHT))

        for lang in LANGUAGES:
            fname = lang.lower().replace("+", "p").replace(" ", "_") + ".png"
            path  = os.path.join(ASSETS_DIR, fname)
            img   = pygame.image.load(path).convert_alpha()
            self._images[lang] = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))

    def setup(self, num_pairs: int = 12):
        """Cria e embaralha as cartas no tabuleiro."""
        self.pairs_found    = 0
        self.total_attempts = 0
        self._face_up.clear()
        self._waiting = False

        chosen = random.sample(LANGUAGES, num_pairs)
        langs  = chosen * 2
        random.shuffle(langs)

        self.cards = []
        for idx, lang in enumerate(langs):
            col = idx % BOARD_COLS
            row = idx // BOARD_COLS
            x   = BOARD_OFFSET_X + col * (CARD_WIDTH + CARD_MARGIN)
            y   = BOARD_OFFSET_Y + row * (CARD_HEIGHT + CARD_MARGIN)
            card = Card(x, y, lang, self._images[lang], self._back_image)
            self.cards.append(card)

    # ── Propriedades ─────────────────────────────────────────
    @property
    def total_pairs(self) -> int:
        return len(self.cards) // 2

    @property
    def is_complete(self) -> bool:
        return self.pairs_found == self.total_pairs

    @property
    def is_locked(self) -> bool:
        """Bloqueia cliques enquanto aguarda fechar cartas erradas ou tem 2 abertas ainda animando."""
        return self._waiting or len(self._face_up) >= 2

    # ── Lógica de clique ─────────────────────────────────────
    def handle_click(self, pos: tuple) -> bool:
        """Retorna True se um clique válido foi processado."""
        if self.is_locked:
            return False

        for card in self.cards:
            if card.contains(pos) and not card.is_face_up and not card.is_matched:
                card.flip()
                self._face_up.append(card)

                if len(self._face_up) == 2:
                    self.total_attempts += 1
                    self._check_pair()
                return True
        return False

    def _check_pair(self):
        a, b = self._face_up
        if a.language == b.language:
            a.is_matched = True
            b.is_matched = True
            self.pairs_found += 1
            self._face_up.clear()
        else:
            # Aguarda antes de virar de volta
            self._waiting    = True
            self._wait_timer = FLIP_DELAY_MS

    # ── Update ───────────────────────────────────────────────
    def update(self, dt: int):
        """dt em milissegundos."""
        for card in self.cards:
            card.update()

        if self._waiting:
            self._wait_timer -= dt
            if self._wait_timer <= 0:
                for card in self._face_up:
                    card.flip()
                self._face_up.clear()
                self._waiting = False

    # ── Draw ─────────────────────────────────────────────────
    def draw(self, surface: pygame.Surface):
        for card in self.cards:
            card.draw(surface)

    # ── Estatísticas ─────────────────────────────────────────
    @property
    def accuracy(self) -> float:
        if self.total_attempts == 0:
            return 0.0
        return round(self.pairs_found / self.total_attempts * 100, 1)
