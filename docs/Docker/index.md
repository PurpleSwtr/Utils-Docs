### Использовать в контейнере порт 8080 TCP

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
