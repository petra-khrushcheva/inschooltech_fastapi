from fastapi import APIRouter

from src.public.router import router as public_router

router = APIRouter(prefix="/v1")
router.include_router(public_router)
