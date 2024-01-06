from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.settings import settings


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(settings.DATABASE_URL)
        self.session_factory = async_sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @asynccontextmanager
    async def get_db(self):
        db: AsyncSession = self.session_factory()
        try:
            yield db
        finally:
            await db.close()


db_helper = DatabaseHelper()
