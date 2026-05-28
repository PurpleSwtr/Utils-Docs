"""
Тут есть предчувствие, что круто было бы создать свой тип для разделов с валидацией, чтобы точно быть уверенным что раздел существует.
"""

import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / ".mkdocsutils" / "config.toml"


def get_categories_names() -> list:
    return [p.name for p in DOCS.iterdir() if p.is_dir()]


def get_sections_names(category: str) -> list:
    return [p.name for p in (DOCS / category).glob("**/*.md") if p.is_file()]


def text_is_code(category: str, categories_codes: dict):
    if category in categories_codes:
        return True
    else:
        return False


def get_raw_text_for_md(
    category: str, title: str, text: str, lang: str = "", code: str = ""
):
    if category not in get_categories_names():
        return

    with open(CONFIG, "rb") as f:
        data = tomllib.load(f)
    categories_codes = data.get("categories_codes", [])

    is_code = text_is_code(category, categories_codes)
    if is_code:
        lang = categories_codes[category]
    if code != "":
        lang = code
    return (
        f"## {title}\n\n```{lang}\n{text}\n```\n"
        if is_code or lang != ""
        else f"## {title}\n\n{text}\n\n"
    )


def write_to_file(text: str, path: Path):
    if not path.exists():
        return ""
    with open(path, "a", encoding="utf-8") as file:
        file.write(text)


def add_to_docs(category: str, section: str, title: str, text: str, code: str = ""):
    path_category = DOCS / category
    path_section = path_category / section
    print(path_section)
    if not path_category.exists() or not path_section.exists():
        return
    write_to_file(
        get_raw_text_for_md(category=category, title=title, text=text, code=code),
        path_section,
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 5:
        # category, section, title, text, [code]
        cat, sec, title, text = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        code = sys.argv[5] if len(sys.argv) > 5 else " "
        result = add_to_docs(cat, sec, title, text, code)
