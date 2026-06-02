import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):
        start_time = time.time()

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{process_time:.2f}ms"
        )

        return response