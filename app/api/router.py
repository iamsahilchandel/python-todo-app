from fastapi import APIRouter

from app.api.v1.routers.root import router as root_router
from app.api.v1.routers.health import router as health_router

router = APIRouter()

router.include_router(root_router, prefix="", tags=["Root"])
router.include_router(health_router, prefix="", tags=["Health"])