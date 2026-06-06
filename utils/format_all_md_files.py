import sys
from pathlib import Path

import mdformat

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

if len(sys.argv) > 1:
    md_files = [Path(p).resolve() for p in sys.argv[1:] if p.endswith(".md")]
else:
    md_files = [p for p in DOCS.rglob("**/*.md") if p.is_file()]

for file_path in md_files:
    try:
        mdformat.file(file_path)
    except Exception as e:
        print(f"{e}")
