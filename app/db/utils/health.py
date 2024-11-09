from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import OperationalError


async def get_postgresql_status(db: AsyncSession) -> bool:

    try:
        exp = await db.execute(select(func.version()))
        exp.scalar()
    except OperationalError:
        return False
    return True
