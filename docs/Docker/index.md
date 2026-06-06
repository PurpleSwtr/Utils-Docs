## Использовать в контейнере порт 8080 TCP

```Dockerfile
EXPOSE 8080
```

## Добавление uv в Dockerfile

```Dockerfile
FROM ghcr.io/astral-sh/uv:0.11.19-python3.13-trixie AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

...

FROM python:3.13-slim-trixie AS runtime
```

## Подключиться к контейнеру из терминала

```Dockerfile
docker exec -it <ID_или_имя_контейнера> bash
```

## Остановка и удаление

```bash
docker compose down
```

## Запуск в фоновом режиме

```bash
docker compose up -d
```

??? note "Фишечка: Принудительное пересоздание"
    Флаг `--force-recreate` - заставить Docker пересоздать контейнеры с нуля, даже если явных изменений не было.

## Сборка без кэша

```bash
docker compose build --no-cache
```

??? tip "Фишечка: Игнорировать кэш"
    Флаг `--no-cache` заставляет Docker игнорировать все закешированные слои при сборке образа.

## Просмотр логов в реальном времени

```bash
docker compose logs -f
```

??? note "Фишечка: Фильтрация и цвет"
    `-f` (follow) для непрерывного вывода.
    `--tail=100` - увидеть только последние 100 строк
    `docker compose logs -f --tail=50 nginx` - имя конкретного сервиса в конце.
