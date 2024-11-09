import uvicorn

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import settings
from api.middleware.exc import HTTPExceptionMiddleware
from api.posts.routers import router as posts_router


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(title='Template', middleware=middleware)
app.add_middleware(HTTPExceptionMiddleware)

app.include_router(
    posts_router,
    prefix=settings.USE_PREFIX,
    tags=['Posts']
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000, log_level="info")
