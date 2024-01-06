from app.core.orm import db_helper
from app.models.posts import PostModel
from repos.base import BaseRepo


class PostRepo(BaseRepo):
    db_model = PostModel
    object_name = 'Post'


posts_repository = PostRepo(db_session=db_helper.get_db)
