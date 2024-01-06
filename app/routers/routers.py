from fastapi import APIRouter

from app.routers.endpoints import (
    posts,
    users,
    auth
)
from app.core.settings import settings

router = APIRouter()

router.include_router(users.router, prefix=settings.API_V1_STR, tags=['Users'])
router.include_router(auth.router, prefix=settings.API_V1_STR, tags=['Auth'])
router.include_router(posts.router, prefix=settings.API_V1_STR, tags=['Posts'])
