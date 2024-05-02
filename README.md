![Workflow badge](https://github.com/petra-khrushcheva/inschooltech_fastapi/actions/workflows/main.yml/badge.svg)

# Inschooltech - Сервис для работы с результатами исследований

Сервис для работы с результатами исследований.
Доступен эндпойнт для получения результатов всех активных завершенных исследований с фильтрацией по id лаборатории ('/v1/tests/tests').
Эндпойнт закрыт авторизацией.
Информация сохраняется в базу данных PostgresQL.
***
### Технологии
Python 3.11  
FastAPI 0.104  
SQLAlchemy 2.0  
Pydantic 2.5  
Alembic 1.13  
PostgreSQL  
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
- Cоздайте переменные окружения по [образцу](https://github.com/petra-khrushcheva/inschooltech_fastapi/blob/main/.env.example).
- Запустите Docker-compose:
```
docker compose -f docker-compose-dev.yml up
``` 