from fastapi import APIRouter, Depends

from app.services.auth import auth_service, get_current_user, get_admin
from app.schemas.users import UserCreateSchema, UserReadSchema, UserDetailSchema

router = APIRouter(prefix='/users')


@router.post('', response_model=UserReadSchema, status_code=201, summary='Создать пользователя')
async def create_user(user_data: UserCreateSchema, current_user=Depends(get_admin)
                      ):
    return await auth_service.register_new_user(user_data)


@router.get('', response_model=UserDetailSchema, status_code=200, summary='Получить инфо о себе')
async def get_user(user: UserReadSchema = Depends(get_current_user)):
    return user
