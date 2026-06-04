from fastapi import APIRouter
from sqlalchemy import text

from app.schemas.health import HealthResponse
from app.db.session import engine

import logging


router = APIRouter()
logger = logging.getLogger(__name__)

async def check_database_connection():
    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
        return True
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        return False


@router.get("/health", response_model=HealthResponse)
async def health():
    is_db_connected = await check_database_connection()
    
    if not is_db_connected:
        return {"status": "unhealthy", "message": "Database connection failed"}
    
    return {"status": "healthy", "message": "API is healthy"}