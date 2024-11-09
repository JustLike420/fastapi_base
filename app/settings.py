import os

from dotenv import load_dotenv
from pydantic import PostgresDsn


load_dotenv()

APP_USERNAME = "admin"

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = PostgresDsn.build(
    scheme='postgresql+asyncpg',
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    path=POSTGRES_DB,
).unicode_string()

USE_PREFIX = os.getenv('USE_PREFIX')

CORS_ORIGINS = [
    'http://localhost',
    'https://localhost',
    'http://localhost:8000',
    'https://localhost:8000',
]
