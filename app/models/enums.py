from enum import Enum


class UserProfileTypeEnum(str, Enum):
    ADMIN = 'admin'
    USER = 'user'
