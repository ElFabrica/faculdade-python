# 🧠 Memory Game — Linguagens de Programação

Jogo da memória em Python orientado a objetos com Pygame.

## Requisitos
```
pip install pygame Pillow
```

## Como executar
```bash
python main.py
```

## Estrutura do Projeto
```
memory_game/
├── main.py                  # Ponto de entrada
├── config.py                # Configurações globais
├── generate_assets.py       # Gerador de imagens das linguagens
├── assets/images/           # Cards PNG (gerados automaticamente)
├── data/
│   └── ranking.txt          # Banco de dados do ranking (pipe-separated)
└── modules/
    ├── card.py              # Classe Card com animação de virada
    ├── board.py             # Classe Board — lógica do tabuleiro
    ├── player.py            # Classe Player — timer e pontuação
    ├── ranking.py           # RankingManager — leitura/escrita TXT
    ├── hud.py               # HUD superior durante o jogo
    ├── screens.py           # Telas: Menu, Nome, Resultado, Ranking
    ├── ui.py                # Componentes UI reutilizáveis
    └── game.py              # Game — máquina de estados principal
```

## Fórmula de pontuação
```
score = pares * 1000 - erros * 100 - tempo_em_segundos * 2
```

## Formato do ranking.txt
```
nome|pontos|pares|tentativas|tempo_segundos|data
```
