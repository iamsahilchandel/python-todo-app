from fastapi import FastAPI

from app.middleware.request_logging import (
    RequestLoggingMiddleware
)


def register_middlewares(
    app: FastAPI
):
    app.add_middleware(
        RequestLoggingMiddleware
    )