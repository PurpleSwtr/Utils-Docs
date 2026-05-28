import re
from pathlib import Path

"""
Может пригодится в будущем, зашить в расширение или типо того.
Было просто интересно написать функцию для поиска, потом уже нашёл что существуют более быстре аналоги на rust...
"""

ROOT = Path(__file__).resolve().parent.parent
PATH_DOCS = ROOT / "docs"


def get_all_files(path: Path) -> list[Path]:
    if not path.is_dir():
        return []
    return [f for f in path.rglob("*") if f.is_file()]


def full_text_search(text: str, base_path: Path = PATH_DOCS) -> list[tuple[Path, int]]:
    search_term = text.strip()
    if not search_term:
        return []

    pattern = re.compile(rf"\b{re.escape(search_term)}\b", re.IGNORECASE)

    results = []
    for file_path in get_all_files(base_path):
        try:
            with file_path.open("r", encoding="utf-8", errors="ignore") as f:
                for line_num, line in enumerate(f, start=1):
                    if pattern.search(line):
                        results.append((file_path, line_num))
        except PermissionError, OSError:
            continue

    return results


print(full_text_search("Спис"))
