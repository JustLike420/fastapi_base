from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.users import TokenBaseSchema
from app.services.auth import auth_service

router = APIRouter(prefix='/auth')


@router.post('/login', response_model=TokenBaseSchema, status_code=200, summary='Авторизация в системе')
async def sign_in(auth_data: OAuth2PasswordRequestForm = Depends()):
    return await auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )
