# Базовый проект

Слоистая архитектура

Controllers,
Services,
Repositories

Dependency Injection,
Unit of Work

Своя реализация авторизации через jwt токен

### Stack
- Python >= 3.10
- FastAPI
- SqlAlchemy 2.0
- Alembic
- Postgres
- Docker

## Установка

### 1. Перейти в папку проекта
Это папка с файлом `main.py`

### 2. Создать и активировать виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```

### 3. Установить зависимости
```
pip install -r requirements.txt
```

### 4. Добавить переменные окружения
```
source .env
```

* DB_NAME: имя БД
* DB_USER: имя пользователя БД
* DB_PASSWORD: пароль пользователя
* DB_HOST: хост БД
* DB_PORT: порт БД
* JWT_SECRET: ключ шифрования токенов
* JWT_ALGORITHM: алгоритм шифрования сигнатуры
* JWT_EXPIRES_S: время жизни токена (в секундах)

### 6. Накатить миграции
```
alembic upgrade head
```


### 7. Стартовать Uvicorn из папки проекта
```
uvicorn main:app --host <host> --port <port>
```
### 8. Создание миграций
```
alembic revision --autogenerate -m "Database init"

alembic upgrade d829eea6e6e6
```
