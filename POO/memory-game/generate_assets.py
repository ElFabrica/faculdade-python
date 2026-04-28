"""
=============================================================
  MODULE: generate_assets.py
  Geração de imagens das linguagens de programação via Pillow
=============================================================
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "images")
CARD_SIZE = (120, 120)

LANGUAGES = [
    {"name": "Python",     "bg": (53, 114, 165),   "fg": (255, 212, 59),  "abbr": "Py"},
    {"name": "JavaScript", "bg": (240, 219, 79),    "fg": (50, 50, 50),    "abbr": "JS"},
    {"name": "TypeScript", "bg": (49, 120, 198),    "fg": (255, 255, 255), "abbr": "TS"},
    {"name": "Rust",       "bg": (36, 34, 35),      "fg": (206, 88, 30),   "abbr": "Rs"},
    {"name": "Go",         "bg": (0, 173, 216),     "fg": (255, 255, 255), "abbr": "Go"},
    {"name": "Java",       "bg": (237, 117, 26),    "fg": (255, 255, 255), "abbr": "Jv"},
    {"name": "C++",        "bg": (0, 89, 157),      "fg": (255, 255, 255), "abbr": "C++"},
    {"name": "Swift",      "bg": (240, 81, 50),     "fg": (255, 255, 255), "abbr": "Sw"},
    {"name": "Kotlin",     "bg": (127, 82, 255),    "fg": (255, 255, 255), "abbr": "Kt"},
    {"name": "Ruby",       "bg": (168, 17, 17),     "fg": (255, 255, 255), "abbr": "Rb"},
    {"name": "PHP",        "bg": (119, 123, 179),   "fg": (255, 255, 255), "abbr": "PHP"},
    {"name": "Dart",       "bg": (0, 180, 216),     "fg": (255, 255, 255), "abbr": "Dt"},
]

BACK_COLOR = (30, 30, 60)
BACK_PATTERN_COLOR = (50, 50, 100)


def generate_card_back():
    img = Image.new("RGB", CARD_SIZE, BACK_COLOR)
    draw = ImageDraw.Draw(img)
    # Draw a simple pattern
    for i in range(0, CARD_SIZE[0], 20):
        draw.line([(i, 0), (0, i)], fill=BACK_PATTERN_COLOR, width=1)
        draw.line([(i, CARD_SIZE[1]), (CARD_SIZE[0], i)], fill=BACK_PATTERN_COLOR, width=1)
    # Border
    draw.rectangle([2, 2, CARD_SIZE[0]-3, CARD_SIZE[1]-3], outline=(100, 100, 180), width=3)
    # Center "?"
    draw.text((CARD_SIZE[0]//2, CARD_SIZE[1]//2), "?", fill=(180, 180, 255), anchor="mm", font=_big_font())
    path = os.path.join(OUTPUT_DIR, "card_back.png")
    img.save(path)
    print(f"  Saved: card_back.png")


def _big_font(size=36):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()


def _small_font(size=14):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()


def generate_language_card(lang: dict):
    img = Image.new("RGB", CARD_SIZE, lang["bg"])
    draw = ImageDraw.Draw(img)

    # Rounded feel via border
    draw.rectangle([2, 2, CARD_SIZE[0]-3, CARD_SIZE[1]-3], outline=lang["fg"], width=3)

    # Abbreviation big in center
    draw.text((CARD_SIZE[0]//2, CARD_SIZE[1]//2 - 10), lang["abbr"],
              fill=lang["fg"], anchor="mm", font=_big_font(34))

    # Full name small at bottom
    draw.text((CARD_SIZE[0]//2, CARD_SIZE[1] - 18), lang["name"],
              fill=lang["fg"], anchor="mm", font=_small_font(13))

    filename = f"{lang['name'].lower().replace('+', 'p').replace(' ', '_')}.png"
    path = os.path.join(OUTPUT_DIR, filename)
    img.save(path)
    print(f"  Saved: {filename}")
    return filename


def generate_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating assets...")
    generate_card_back()
    mapping = {}
    for lang in LANGUAGES:
        fname = generate_language_card(lang)
        mapping[lang["name"]] = fname
    print(f"Done. {len(LANGUAGES)} language cards + back generated.")
    return mapping


if __name__ == "__main__":
    generate_all()
