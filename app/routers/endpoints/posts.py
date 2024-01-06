from typing import List, Optional

from fastapi import APIRouter, Depends

from app.schemas.posts import PostCreateSchema, PostReadSchema, PostDetailSchema, PostUpdateSchema

from app.services.posts_service import posts_service

router = APIRouter(prefix='/posts')


@router.post("/create", response_model=PostReadSchema, status_code=201, summary='Создать пост')
async def create_post(class_type_data: PostCreateSchema):
    return await posts_service.create_post(class_type_data)


@router.get("/all", response_model=List[PostReadSchema], status_code=200, summary='Посмотреть все посты')
async def get_posts(
        # current_user=Depends(get_current_user)
                    ):
    return await posts_service.get_posts()


@router.get("/{post_id}", response_model=Optional[PostReadSchema], status_code=200, summary='Посмотреть отдельный пост')
async def get_post(post_id: int):
    return await posts_service.get_post_by_id(post_id)


@router.put("/{post_id}", response_model=PostReadSchema, status_code=200, summary='Посмотреть отдельный пост')
async def update_post(post_id: int, class_type_data: PostUpdateSchema):
    return await posts_service.update_post(post_id, class_type_data)


@router.delete("/{post_id}", status_code=200, summary='Удалить отдельный пост')
async def delete_post(post_id: int):
    return await posts_service.delete_post(post_id)
