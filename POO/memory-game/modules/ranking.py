"""
=============================================================
  MODULE: modules/ranking.py
  Classe RankingManager — leitura e gravação do ranking em TXT
  Formato do arquivo: nome|pontos|pares|tentativas|tempo|data
=============================================================
"""

import os
from datetime import datetime
from config import RANKING_FILE, DATA_DIR


class RankingEntry:
    """Representa uma entrada no ranking."""

    SEPARATOR = "|"

    def __init__(self, name: str, score: int, pairs: int,
                 attempts: int, elapsed: float, date: str):
        self.name     = name
        self.score    = score
        self.pairs    = pairs
        self.attempts = attempts
        self.elapsed  = elapsed
        self.date     = date

    @classmethod
    def from_line(cls, line: str) -> "RankingEntry | None":
        parts = line.strip().split(cls.SEPARATOR)
        if len(parts) != 6:
            return None
        try:
            return cls(
                name     = parts[0],
                score    = int(parts[1]),
                pairs    = int(parts[2]),
                attempts = int(parts[3]),
                elapsed  = float(parts[4]),
                date     = parts[5],
            )
        except ValueError:
            return None

    def to_line(self) -> str:
        return self.SEPARATOR.join([
            self.name,
            str(self.score),
            str(self.pairs),
            str(self.attempts),
            str(self.elapsed),
            self.date,
        ])

    @property
    def elapsed_str(self) -> str:
        secs = int(self.elapsed)
        return f"{secs // 60:02d}:{secs % 60:02d}"

    @property
    def accuracy(self) -> float:
        if self.attempts == 0:
            return 0.0
        return round(self.pairs / self.attempts * 100, 1)


class RankingManager:
    """Gerencia o arquivo TXT de ranking."""

    MAX_ENTRIES = 100  # Limite de entradas salvas

    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(RANKING_FILE):
            open(RANKING_FILE, "w").close()

    # ── Leitura ──────────────────────────────────────────────
    def load(self) -> list[RankingEntry]:
        entries = []
        try:
            with open(RANKING_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        entry = RankingEntry.from_line(line)
                        if entry:
                            entries.append(entry)
        except FileNotFoundError:
            pass
        # Ordena por pontuação desc
        entries.sort(key=lambda e: e.score, reverse=True)
        return entries

    # ── Gravação ─────────────────────────────────────────────
    def save_entry(self, name: str, score: int, pairs: int,
                   attempts: int, elapsed: float):
        entry = RankingEntry(
            name     = name,
            score    = score,
            pairs    = pairs,
            attempts = attempts,
            elapsed  = elapsed,
            date     = datetime.now().strftime("%d/%m/%Y %H:%M"),
        )
        entries = self.load()
        entries.append(entry)
        entries.sort(key=lambda e: e.score, reverse=True)
        entries = entries[:self.MAX_ENTRIES]

        with open(RANKING_FILE, "w", encoding="utf-8") as f:
            for e in entries:
                f.write(e.to_line() + "\n")

    # ── Posição do jogador ───────────────────────────────────
    def get_position(self, score: int) -> int:
        entries = self.load()
        for i, e in enumerate(entries):
            if e.score == score:
                return i + 1
        return len(entries)
