from sqlalchemy import select, update, delete
from starlette import status
from app.dependencies.rep_dep import IAsyncSession
from fastapi import HTTPException


class BaseRepo:
    object_name = 'Object'

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def create_object(self, obj_data_dict=None):
        async with self._session() as session:
            instance = self.db_model(**obj_data_dict.model_dump())
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def get_object(self, filters: dict = {}):
        async with self._session() as session:
            row = await session.execute(select(self.db_model).filter_by(**filters))
            return row.scalar_one_or_none()

    async def get_objects(self, filter: dict = {}):
        async with self._session() as session:
            stmt = select(self.db_model).filter_by(**filter)
            res = await session.execute(stmt)
            res = res.scalars().all()
        return res

    async def update_object(self, filters: dict, obj_data_dict=None):
        async with self._session() as session:
            stmt = update(self.db_model).values(**obj_data_dict.model_dump()).filter_by(**filters).returning(
                self.db_model)
            obj = await session.execute(stmt)
            result = obj.fetchone()
            if obj:
                await session.commit()
                return result
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def delete_object(self, filters: dict):
        async with self._session() as session:
            obj = await session.execute(delete(self.db_model).filter_by(**filters))
            if obj.rowcount == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            await session.commit()
