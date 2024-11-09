from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.posts.helpers import get_posts_by_id
from api.posts.schemas import PostReadSchema, PostCreateSchema, PostDetailSchema, PostUpdateSchema
from db.session import get_db
from service.posts import handlers as posts_handlers


router = APIRouter(prefix='/posts')


@router.post("", response_model=PostReadSchema)
async def create_post(post: PostCreateSchema, db: AsyncSession = Depends(get_db)):
    return await posts_handlers.create_post(db, post)


@router.get("", response_model=list[PostReadSchema])
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await posts_handlers.get_posts(db)


@router.get("/{post_id}", response_model=PostDetailSchema)
async def get_post(post=Depends(get_posts_by_id)):
    return post


#
#
@router.put("/{post_id}", response_model=PostReadSchema)
async def update_post(
    class_type_data: PostUpdateSchema,
    post=Depends(get_posts_by_id),
    db: AsyncSession = Depends(get_db)
):
    return await posts_handlers.update_post(db, post, class_type_data)


#
@router.delete("/{post_id}")
async def delete_post(post=Depends(get_posts_by_id), db: AsyncSession = Depends(get_db)):
    return await posts_handlers.delete_post(db, post.id)
