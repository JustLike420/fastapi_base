from sqlalchemy import String, Column, Integer

from db.meta import Base
from db.mixins.timestamp import UpdatedAtMixin


class Post(Base, UpdatedAtMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    text = Column(String)
