"""
=============================================================
  MODULE: modules/card.py
  Classe Card — representa uma carta individual do jogo
=============================================================
"""

import pygame
from config import (
    CARD_WIDTH, CARD_HEIGHT, COLOR_CARD_BG, COLOR_BORDER,
    COLOR_SUCCESS, FLIP_ANIM_STEPS
)


class Card:
    """Carta do jogo da memória com animação de virada."""

    def __init__(self, x: int, y: int, language: str, image_front: pygame.Surface, image_back: pygame.Surface):
        self.x = x
        self.y = y
        self.language = language
        self.image_front = image_front
        self.image_back  = image_back

        self.is_face_up   = False
        self.is_matched   = False
        self.is_animating = False

        # Animação de virada (escala horizontal de 1 → 0 → 1)
        self._anim_step      = 0
        self._anim_direction = 1   # 1 = abrindo, -1 = fechando
        self._target_face_up = False

    # ── Rect ────────────────────────────────────────────────
    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)

    # ── Estado ──────────────────────────────────────────────
    def flip(self):
        """Inicia animação de virada."""
        if self.is_matched or self.is_animating:
            return
        self._target_face_up = not self.is_face_up
        self.is_animating    = True
        self._anim_step      = 0
        self._anim_direction = 1

    def instant_flip(self, face_up: bool):
        """Vira sem animação (usado em reset)."""
        self.is_face_up = face_up
        self.is_animating = False
        self._anim_step = 0

    # ── Update ──────────────────────────────────────────────
    def update(self):
        if not self.is_animating:
            return

        self._anim_step += self._anim_direction

        # Ponto de virada: muda face na metade da animação
        if self._anim_step == FLIP_ANIM_STEPS // 2:
            self.is_face_up = self._target_face_up

        if self._anim_step >= FLIP_ANIM_STEPS:
            self.is_animating = False
            self._anim_step   = 0

    # ── Draw ────────────────────────────────────────────────
    def draw(self, surface: pygame.Surface):
        # Escala horizontal para simular rotação 3D
        if self.is_animating:
            half  = FLIP_ANIM_STEPS // 2
            phase = abs(self._anim_step - half)  # 0..half
            scale = phase / half                  # 0..1
            w     = max(2, int(CARD_WIDTH * scale))
        else:
            w = CARD_WIDTH

        cx = self.x + CARD_WIDTH // 2
        cy = self.y + CARD_HEIGHT // 2

        img = self.image_front if self.is_face_up else self.image_back
        scaled = pygame.transform.scale(img, (w, CARD_HEIGHT))
        rect   = scaled.get_rect(center=(cx, cy))
        surface.blit(scaled, rect)

        # Borda destacada para cartas combinadas
        if self.is_matched:
            border_rect = pygame.Rect(self.x - 2, self.y - 2, CARD_WIDTH + 4, CARD_HEIGHT + 4)
            pygame.draw.rect(surface, COLOR_SUCCESS, border_rect, 3, border_radius=8)
        else:
            border_rect = pygame.Rect(self.x - 1, self.y - 1, CARD_WIDTH + 2, CARD_HEIGHT + 2)
            pygame.draw.rect(surface, COLOR_BORDER, border_rect, 1, border_radius=8)

    # ── Colisão ─────────────────────────────────────────────
    def contains(self, pos: tuple) -> bool:
        return self.rect.collidepoint(pos)
