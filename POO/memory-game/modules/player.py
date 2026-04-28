"""
=============================================================
  MODULE: modules/player.py
  Classe Player — dados e pontuação do jogador atual
=============================================================
"""

import time


class Player:
    """Representa o jogador na sessão atual."""

    def __init__(self, name: str):
        self.name       = name.strip()[:20]  # Limite de 20 chars
        self._start_time: float | None = None
        self._end_time:   float | None = None

    # ── Timer ────────────────────────────────────────────────
    def start_timer(self):
        self._start_time = time.time()
        self._end_time   = None

    def stop_timer(self):
        self._end_time = time.time()

    @property
    def elapsed_seconds(self) -> float:
        if self._start_time is None:
            return 0.0
        end = self._end_time if self._end_time else time.time()
        return round(end - self._start_time, 1)

    @property
    def elapsed_str(self) -> str:
        secs  = int(self.elapsed_seconds)
        mins  = secs // 60
        secs  = secs % 60
        return f"{mins:02d}:{secs:02d}"

    # ── Pontuação ────────────────────────────────────────────
    def compute_score(self, pairs_found: int, total_attempts: int, elapsed: float) -> int:
        """
        Fórmula: pares * 1000 - tentativas_erradas * 100 - tempo_em_segundos * 2
        Mínimo 0.
        """
        errors = max(0, total_attempts - pairs_found)
        score  = pairs_found * 1000 - errors * 100 - int(elapsed * 2)
        return max(0, score)
