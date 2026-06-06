"""
Тут есть предчувствие, что круто было бы создать свой тип для разделов с валидацией, чтобы точно быть уверенным что раздел существует.
"""

import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / ".mkdocsutils" / "config.toml"


def get_categories_names() -> list:
    with open(CONFIG, "rb") as f:
        data = tomllib.load(f)
    exclude_directories = data.get("excluded_directories", {}).get("dirs", [])
    return [
        p.name
        for p in DOCS.iterdir()
        if p.is_dir() and p.name not in exclude_directories
    ]


def get_sections_names(category: str) -> list:
    return [p.name for p in (DOCS / category).glob("**/*.md") if p.is_file()]


def text_is_code(category: str, categories_codes: dict) -> bool:
    return category in categories_codes


def get_raw_text_for_md(
    category: str,
    title: str,
    text: str,
    is_note: bool,
    lang: str = "",
    code: str = "",
) -> str | None:
    if category not in get_categories_names():
        return None

    if is_note:
        return f"\n## {title}\n\n{text}\n"

    with open(CONFIG, "rb") as f:
        data = tomllib.load(f)
    categories_codes = data.get("categories_codes", {})

    is_code = text_is_code(category, categories_codes)
    if is_code:
        lang = categories_codes[category]
    if code != "":
        lang = code

    return f"\n## {title}\n\n```{lang}\n{text}\n```\n"


def write_to_file(text: str, path: Path) -> None:
    if not path.exists():
        return
    with open(path, "a", encoding="utf-8") as file:
        file.write(text)


def add_to_docs(
    category: str,
    section: str,
    title: str,
    text: str,
    is_note: bool,
    code: str | None = "",
) -> None | FileNotFoundError:
    path_category = DOCS / category
    path_section = path_category / section

    if not path_category.exists():
        raise FileNotFoundError(category)
    if not path_section.exists():
        raise FileNotFoundError(section)

    raw_text = get_raw_text_for_md(
        category=category,
        title=title,
        text=text,
        code=code or "",
        is_note=is_note,
    )
    if raw_text:
        write_to_file(raw_text, path_section)


def get_md_text(category: str, section: str) -> str:
    path_category = DOCS / category
    path_section = path_category / section
    if not path_category.exists():
        raise FileNotFoundError(category)
    if not path_section.exists():
        raise FileNotFoundError(section)
    with open(file=path_section, mode="r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 5:
        cat, sec, title, text = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        code = sys.argv[5] if len(sys.argv) > 5 else ""
        is_note = sys.argv[6].lower() == "true" if len(sys.argv) > 6 else False
        add_to_docs(
            category=cat,
            section=sec,
            title=title,
            text=text,
            is_note=is_note,
            code=code,
        )
