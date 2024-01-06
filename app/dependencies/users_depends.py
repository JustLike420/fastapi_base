from typing import Annotated

from fastapi import Depends

from repos.users import UserRepo

IUserRepository = Annotated[UserRepo, Depends(UserRepo)]
