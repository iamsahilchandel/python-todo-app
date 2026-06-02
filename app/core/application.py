from fastapi import FastAPI

from app.core.config import settings
from app.core.constants import API_V1_PREFIX
from app.core.lifespan import lifespan
from app.api.router import router as api_router




"""
Application factory function to create and configure the FastAPI app.
This function initializes the FastAPI application, sets up the API routes,
and returns the configured app instance.
"""
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.include_router(api_router, prefix=API_V1_PREFIX)

    return app