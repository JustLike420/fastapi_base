from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.exceptions.posts import post_object_not_found
from db.session import get_db
from service.posts.models import Post


async def get_posts_by_id(post_id: int, db: AsyncSession = Depends(get_db)):
    obj_exp = await db.execute(select(Post).where(Post.id == post_id))
    obj = obj_exp.scalars().one_or_none()

    if not obj:
        raise post_object_not_found

    return obj
