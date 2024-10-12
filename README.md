# [Проект QRKot.](https://github.com/QuickLike/cat_charity_fund)

## Технологии:

- Python
- FastAPI

## Описание проекта:

QRKot - Фонд, который собирает пожертвования на различные целевые проекты:
на медицинское обслуживание нуждающихся хвостатых,
на обустройство кошачьей колонии в подвале,
на корм оставшимся без попечения кошкам — на любые цели,
связанные с поддержкой кошачьей популяции.

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/QuickLike/cat_charity_fund) и перейдите в него в командной строке:
```
git clone https://github.com/QuickLike/cat_charity_fund

cd cat_charity_fund
```
Создайте виртуальное окружение и активируйте его

Windows
```
python -m venv venv
venv/Scripts/activate
```

Linux/Ubuntu/MacOS
```
python3 -m venv venv
source venv/bin/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
В корне проекта создайте файл .env, и добавьте туда переменные окружения
```
APP_TITLE=Кошачий благотворительный фонд.
DESCRIPTION=Сервис для пожертвования кошкам на различные услуги, связанные с поддержкой кошачьей популяции.
DATABASE_URL=sqlite+aiosqlite:///./catcharity.db
FIRST_SUPERUSER_EMAIL=<имя_суперпользователя>
FIRST_SUPERUSER_PASSWORD=<пароль_суперпользователя>
SECRET=<секретный_ключ>
```

Применить миграции
```
alembic upgrade head
```
Запуск проекта
```
uvicorn app.main:app --reload
```

### Документация будет доступна по следующим адресам:

[Swagger](https://127.0.0.1:8000/docs)

[OpenAPI](https://127.0.0.1:8000/redoc)


## Автор

[Власов Эдуард](https://github.com/QuickLike)
