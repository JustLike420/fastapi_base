from datetime import (
    datetime,
    timedelta,
)
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from jose import jwt, ExpiredSignatureError, JWTError
from passlib.hash import bcrypt

from app.core.exceptions import (
    IncorrectPasswordException,
    UserNotFoundException,
    TokenExpiredException,
    ValidateCredentialsException,
    NoRightsException
)
from app.core.settings import settings
from app.dependencies.users_depends import IUserRepository
from app.schemas.users import UserCreateSchema, TokenBaseSchema, UserDetailSchema
from app.services.users_service import users_service
from repos.users import users_repository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.API_V1_STR + '/auth/login')


async def get_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )

    except ExpiredSignatureError:
        raise TokenExpiredException

    user_obj = await users_service.get_user(int(payload["sub"]))
    if not user_obj.profile_type == 'admin':
        raise NoRightsException
    return AuthService.verify_token(token)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )

    except ExpiredSignatureError:
        raise TokenExpiredException

    return AuthService.verify_token(token)


class AuthService:

    def __init__(self, users_repository: IUserRepository) -> None:
        self.users_repository = users_repository

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_token(cls, token: str) -> UserDetailSchema:
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=[settings.JWT_ALGORITHM],
            )
        except JWTError:
            raise ValidateCredentialsException from None

        user_data = payload.get('user')

        try:
            user = UserDetailSchema.parse_obj(user_data)
        except ValidationError:
            raise ValidateCredentialsException from None

        return user

    async def register_new_user(self, user: UserCreateSchema):

        user.password = self.hash_password(user.password)
        return await self.users_repository.create_object(user)

    @classmethod
    def create_token(cls, user) -> TokenBaseSchema:
        user_id = user.id

        now = datetime.utcnow()
        # custom information
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(days=settings.JWT_EXPIRES_DAY),
            'sub': str(user_id),
            'user': {"id": user_id, "email": user.email},  # change to pydantic model
        }
        token = jwt.encode(
            payload,
            settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM,
        )
        return TokenBaseSchema(access_token=token, profile_type=user.profile_type)

    async def authenticate_user(self, username: str, password: str) -> TokenBaseSchema:
        user = await self.users_repository.get_object(filters={"email": username})

        if not user:
            raise UserNotFoundException

        if not self.verify_password(password, user.password):
            raise IncorrectPasswordException

        return self.create_token(user)


auth_service = AuthService(users_repository=users_repository)
