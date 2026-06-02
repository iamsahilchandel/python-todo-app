from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    AppException
)

def register_exception_handlers(
    app: FastAPI
):

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request,
        exc
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": exc.message
            }
        )