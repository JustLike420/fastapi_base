from sqlalchemy.orm import Mapped
from .base import Base


class PostModel(Base):
    __tablename__ = "posts"

    name: Mapped[str]
    text: Mapped[str]
