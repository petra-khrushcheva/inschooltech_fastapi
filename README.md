![Workflow badge](https://github.com/petra-khrushcheva/inschooltech_fastapi/actions/workflows/main.yml/badge.svg)

# Inschooltech - Сервис для работы с результатами исследований

Сервис для работы с результатами исследований.
Доступен эндпойнт для получения результатов всех активных завершенных исследований с фильтрацией по id лаборатории ('/v1/tests/tests_by_lab').
Эндпойнт закрыт авторизацией.
Информация сохраняется в базу данных PostgresQL.
***
### Технологии
Python 3.11  
FastAPI 0.104  
SQLAlchemy 2.0
***
### Установка
- Клонируйте проект:
```
git clone git@github.com:petra-khrushcheva/inschooltech_fastapi.git
``` 
- Перейдите в директорию inschooltech_fastapi:
```
cd inschooltech_fastapi
``` 
- Cоздайте .env файл по образцу:
```
DB_HOSTNAME=
DB_PORT=
DB_USERNAME=
DB_PASSWORD=
DB_NAME=
DB_ECHO=False
SECRET_KEY=

PROJECT_NAME="Inschooltech"
PROJECT_VERSION="0.1.0"
JWT_LIFETIME_SECONDS=2592000 #1 month

``` 
- Запустите Docker-compose:
```
docker compose -f docker-compose-dev.yml up
``` 