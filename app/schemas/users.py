from pydantic import BaseModel, EmailStr

from app.models.enums import UserProfileTypeEnum


class UserBaseSchema(BaseModel):
    profile_type: UserProfileTypeEnum
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    email: EmailStr
    profile_type: UserProfileTypeEnum
    password: str


class UserReadSchema(UserBaseSchema):
    id: int
    email: EmailStr


class UserDetailSchema(BaseModel):
    id: int
    email: EmailStr


class TokenBaseSchema(BaseModel):
    access_token: str
    token_type: str = 'Bearer'
    profile_type: UserProfileTypeEnum


class UserTokenPayloadSchema(UserBaseSchema):
    id: int
