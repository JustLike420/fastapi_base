from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from api.posts.schemas import PostCreateSchema, PostUpdateSchema
from db.utils.transactional import transaction
from service.posts.models import Post


async def create_post(db: AsyncSession, post: PostCreateSchema):
    async with transaction(db):
        new_post = Post(name=post.name, text=post.text)

        db.add(new_post)

    await db.refresh(new_post)
    return new_post


async def get_posts(db: AsyncSession):
    obj_exp = await db.execute(select(Post))
    return obj_exp.scalars().all()


async def update_post(db: AsyncSession, post: Post, post_schema: PostUpdateSchema):

    await db.execute(
        update(Post)
        .where(Post.id == post.id)
        .values(**post_schema.model_dump())
    )
    await db.refresh(post)
    return post


async def delete_post(db: AsyncSession, post_id: int):
    await db.execute(delete(Post).where(Post.id == post_id))
