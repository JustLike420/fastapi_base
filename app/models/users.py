from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .enums import UserProfileTypeEnum


class UserModel(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str]
    profile_type: Mapped[UserProfileTypeEnum]
