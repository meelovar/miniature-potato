Запуск проверялся с `docker-ce` версии 26.1 и Python 3.12.

# Запуск c Docker

1. Сборка образа

```shell
docker build -f docker/Dockerfile -t test_task_aiohttp .
```

2. Запуск

```
docker run --rm -p 8000:8000 test_task_aiohttp
```

Сервер будет расположен по адресу http://localhost:8000

# Запуск без Docker

Для установки зависимостей должен быть установлен `poetry`.

1. Установка зависимостей (вместе с `pytest`)

```shell
poetry install --with dev
```

2. Запуск (для запуска директория `src` должна находиться в `PYTHONPATH`)

```shell
PYTHONPATH=./src poetry run python3 -m main
```

# Запуск тестов

Директория `src` должна находиться в `PYTHONPATH`.

```shell
PYTHONPATH=./src poetry run pytest
```
