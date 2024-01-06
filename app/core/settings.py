from typing import (
    Any,
    Dict,
    Optional,
)

from pydantic import (
    PostgresDsn,
    field_validator,
)
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Class with project settings and variables."""

    # version API
    API_V1_STR: str = '/api/v1'

    # DB
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DATABASE_URL: Optional[str] = None

    # Auth
    JWT_SECRET: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRES_DAY: int = 7

    @field_validator('DATABASE_URL', mode="before")
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        """Create URL for DB connect"""
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=values.data.get('DB_USER'),
            password=values.data.get('DB_PASSWORD'),
            host=values.data.get('DB_HOST'),
            # port=values.data.get('DB_PORT'),
            path=f'{values.data.get("DB_NAME") or ""}',
        ).unicode_string()


settings = Settings()
