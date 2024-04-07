from fastapi import APIRouter, Depends

from src.public.router import router as public_router
from src.users.dependencies import current_active_user as current_user
from src.users.router import router as users_router

router = APIRouter(prefix="/v1", dependencies=[Depends(current_user)])
router.include_router(public_router)
router.include_router(users_router)
