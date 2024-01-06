from app.core.orm import db_helper
from app.models.users import UserModel
from repos.base import BaseRepo


class UserRepo(BaseRepo):
    db_model = UserModel
    object_name = 'User'


users_repository = UserRepo(db_session=db_helper.get_db)
