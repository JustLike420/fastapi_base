from pydantic import BaseModel


class PostBase(BaseModel):
    name: str
    text: str


class PostReadSchema(BaseModel):
    id: int
    name: str


class PostDetailSchema(PostBase):
    id: int


class PostUpdateSchema(PostBase):
    pass


class PostCreateSchema(PostBase):
    pass
