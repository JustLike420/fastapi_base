from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine
)

import settings


engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)
async_session = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_db() -> AsyncGenerator:
    try:
        session: AsyncSession = async_session()
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
    finally:
        await session.close()
