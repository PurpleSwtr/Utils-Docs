## Установка

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Генерация requirements.txt с помощью uv

```bash
uv export --format requirements-txt > requirements.txt
```

## Добавить все зависимости из requirements.txt в проект с помощью uv

```bash
uv add -r requirements.txt
```
