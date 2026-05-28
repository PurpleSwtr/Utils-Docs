### Получить директорию файла

```python
import os

# Полный путь к текущему файлу
current_file_path = os.path.abspath(__file__)

# Где находится текущий файл
current_dir = os.path.dirname(current_file_path)

# На уровень выше соответственно
parent_dir = os.path.dirname(current_dir)
```

### Создать путь для любой OC

```python
dir = os.path.join(current_dir, config.docs_dir_name)
```

### Пройтись по всем поддиректориям/файлам в директории

```python
start_directory = 'Тут начальный путь'

# os.walk() возвращает генератор
for current_path, subdirectories, files in os.walk(start_directory):
    for file in files:
        print(os.path.join(current_path, file))
```

### Поиск всех файлов в папке и подпапках

```python
from pathlib import Path

folder_path = Path(...)

for file_path in folder_path.rglob("*"):
    if file_path.is_file():
        print(file_path)
```

### Имя файла без расширения

```python
from pathlib import Path
Path("folder/file.txt").stem   # 'file'
```

### Прочитать все файлы в папке

```python
for p in Path("my_dir").iterdir():
    if p.is_file():
        print(p)
```

### Чтение/запись TOML (Python 3.11+)

```python
import tomllib
with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
deps = data.get("dependencies", [])
```

### Сгенерировать `requirements.txt` из `pyproject.toml`

```python
import tomllib
with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
with open("requirements.txt", "w") as f:
    for dep in data.get("dependencies", []):
        f.write(dep + "\n")
```

### Изменить переменную в `.env` файле

```python
from dotenv import set_key
set_key(".env", "TASK", "123")
```

### Чтение `.env` и переменных окружения

```python
from dotenv import load_dotenv
import os
load_dotenv()
task = os.getenv("TASK")
```
