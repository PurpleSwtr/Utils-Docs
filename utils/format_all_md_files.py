from pathlib import Path

import mdformat

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

md_files = [p for p in DOCS.rglob("**/*.md") if p.is_file()]

for file_path in md_files:
    try:
        mdformat.file(file_path)
    except Exception as e:
        print(f"{e}")
