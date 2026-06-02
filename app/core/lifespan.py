from contextlib import asynccontextmanager

from app.core.logging_config import setup_logging

import logging


@asynccontextmanager
async def lifespan(app):
    setup_logging()
    logger = logging.getLogger(__name__)

    # Startup code here (e.g., connect to database, initialize resources)
    logger.info("Starting up the application...")
    
    yield
    
    # Shutdown code here (e.g., close database connections, clean up resources)
    logger.info("Shutting down the application...")