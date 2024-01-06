from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.core.orm import db_helper
from fastapi import Depends

IAsyncSession = Annotated[AsyncSession, Depends(db_helper.get_db)]
