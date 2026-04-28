"""
=============================================================
  MODULE: modules/ui.py
  Funções utilitárias de UI — fontes, botões, painéis
=============================================================
"""

import pygame
from config import (
    COLOR_TEXT, COLOR_MUTED, COLOR_PRIMARY, COLOR_PANEL,
    COLOR_BORDER
)

_font_cache: dict = {}


def get_font(size: int, bold: bool = False) -> pygame.font.Font:
    key = (size, bold)
    if key not in _font_cache:
        try:
            _font_cache[key] = pygame.font.SysFont("arial", size, bold=bold)
        except Exception:
            _font_cache[key] = pygame.font.Font(None, size)
    return _font_cache[key]


def draw_text(surface, text: str, x: int, y: int, size: int = 20,
              color=COLOR_TEXT, bold: bool = False, anchor: str = "topleft"):
    font   = get_font(size, bold)
    render = font.render(text, True, color)
    rect   = render.get_rect(**{anchor: (x, y)})
    surface.blit(render, rect)
    return rect


def draw_panel(surface, rect: pygame.Rect, color=COLOR_PANEL,
               border_color=COLOR_BORDER, radius: int = 12):
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    pygame.draw.rect(surface, border_color, rect, 1, border_radius=radius)


class Button:
    def __init__(self, x, y, w, h, label, color=COLOR_PRIMARY,
                 text_color=COLOR_TEXT, font_size=20, radius=10):
        self.rect        = pygame.Rect(x, y, w, h)
        self.label       = label
        self.color       = color
        self.hover_color = tuple(min(255, c + 40) for c in color)
        self.text_color  = text_color
        self.font_size   = font_size
        self.radius      = radius
        self._hovered    = False

    def draw(self, surface: pygame.Surface):
        color = self.hover_color if self._hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=self.radius)
        pygame.draw.rect(surface, COLOR_BORDER, self.rect, 1, border_radius=self.radius)
        draw_text(surface, self.label,
                  self.rect.centerx, self.rect.centery,
                  self.font_size, self.text_color, bold=True, anchor="center")

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEMOTION:
            self._hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class TextInput:
    def __init__(self, x, y, w, h, placeholder="", max_len=20):
        self.rect        = pygame.Rect(x, y, w, h)
        self.placeholder = placeholder
        self.max_len     = max_len
        self.text        = ""
        self.active      = False
        self._cursor_vis  = True
        self._cursor_tick = 0

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key not in (pygame.K_RETURN, pygame.K_TAB):
                if len(self.text) < self.max_len and event.unicode.isprintable():
                    self.text += event.unicode

    def update(self):
        self._cursor_tick += 1
        if self._cursor_tick >= 30:
            self._cursor_vis  = not self._cursor_vis
            self._cursor_tick = 0

    def draw(self, surface: pygame.Surface):
        border = COLOR_PRIMARY if self.active else COLOR_BORDER
        pygame.draw.rect(surface, COLOR_PANEL, self.rect, border_radius=8)
        pygame.draw.rect(surface, border, self.rect, 2, border_radius=8)

        font   = get_font(22, bold=True)
        disp   = self.text if self.text else self.placeholder
        color  = COLOR_TEXT if self.text else COLOR_MUTED
        render = font.render(disp, True, color)
        surface.blit(render, (self.rect.x + 12, self.rect.y + (self.rect.height - render.get_height()) // 2))

        if self.active and self._cursor_vis and self.text:
            cur_x = self.rect.x + 12 + render.get_width() + 2
            cur_y = self.rect.y + 8
            pygame.draw.line(surface, COLOR_TEXT,
                             (cur_x, cur_y), (cur_x, cur_y + self.rect.height - 16), 2)