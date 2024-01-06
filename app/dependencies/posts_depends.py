from typing import Annotated

from fastapi import Depends

from repos.posts import PostRepo

# from src.config.database.db_helper import db_helper


IPostRepository = Annotated[PostRepo, Depends(PostRepo)]
