from app.dependencies.posts_depends import IPostRepository
from app.schemas.posts import PostCreateSchema, PostUpdateSchema
from repos.posts import posts_repository


class PostsService:

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def create_post(self, post: PostCreateSchema):
        return await self.repository.create_object(post)

    async def get_posts(self):
        return await self.repository.get_objects()

    async def get_post_by_id(self, post_id: int):
        return await self.repository.get_object(filters={'id': post_id})

    async def update_post(self, post_id: int, post: PostUpdateSchema):
        return await self.repository.update_object({'id': post_id}, post)

    async def delete_post(self, post_id: int):
        return await self.repository.delete_object({'id': post_id})


posts_service = PostsService(posts_repository)
