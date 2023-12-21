from fastapi import FastAPI

from src.config import settings
from src.public.router import router as public_router

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version
)

app.include_router(public_router)
