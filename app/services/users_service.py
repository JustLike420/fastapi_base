from app.dependencies.users_depends import IUserRepository
from app.schemas.users import UserCreateSchema
from repos.users import users_repository


class UsersService:

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    async def create_user(self, user: UserCreateSchema):
        return await self.repository.create_object(user)

    async def get_user(self, user_id: int):
        return await self.repository.get_object(filters={"id": user_id})


users_service = UsersService(users_repository)
