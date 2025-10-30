## Получить директорию файла

```python
import os

# Полный путь к текущему файлу
current_file_path = os.path.abspath(__file__) 

# Где находится текущий файл
current_dir = os.path.dirname(current_file_path) 

# На уровень выше соответственно
parent_dir = os.path.dirname(current_dir)
```

## Создать путь для любой OC

```python
dir = os.path.join(current_dir, config.docs_dir_name)
```

## Пройтись по всем поддиректориям/файлам в директории

```python
start_directory = 'Тут путь начальный'

# os.walk() возвращает генератор
for current_path, subdirectories, files in os.walk(start_directory):
    for file in files:
        print(os.path.join(current_path, file))
```