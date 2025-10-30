from pathlib import Path
import re
from config import config

def get_real_docs_files(docs_dir: str) -> set:
    found_files = set()
    docs_path = Path(docs_dir)

    for file_path in docs_path.rglob("*.md"):
        relative_path = file_path.relative_to(docs_path).as_posix()
        found_files.add(relative_path)

    return found_files

def get_mkdocs_nav_files(mkdocs_yml_path: str) -> set:
    nav_files = set()
    pattern = re.compile(r":\s*['\"]?([^'\"]+\.md)['\"]?")
    try:
        with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == "" and nav_files:
                    break
                match = pattern.search(line)
                if match:
                    nav_files.add(match.group(1))
    except FileNotFoundError:
        print(f"Файл {mkdocs_yml_path} не найден.")
        return set()

    return nav_files

def main():
    current_script_path = Path(__file__).resolve()
    project_dir = current_script_path.parent.parent

    docs_dir = project_dir / config.docs_dir_name
    mkdocs_yml_path = project_dir / 'mkdocs.yml'

    real_files = get_real_docs_files(str(docs_dir))
    nav_files = get_mkdocs_nav_files(str(mkdocs_yml_path))

    if real_files == nav_files:
        print("Изменений нет!")
        return

    untracked_files = real_files - nav_files
    if untracked_files:
        print("Не добавленные в mkdocs.yml:")
        for f in sorted(untracked_files):
            print(f" - {f}")

    missing_files = nav_files - real_files
    if missing_files:
        for file_to_create in sorted(missing_files):
            try:
                full_path = docs_dir / file_to_create
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.touch()
                print(f" - Файл '{file_to_create}' создан.")
            except OSError as e:
                print(e)

if __name__ == "__main__":
    main()