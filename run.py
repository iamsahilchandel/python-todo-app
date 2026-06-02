import argparse
import uvicorn

from app.core.config import settings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reload", action="store_true", default=settings.debug)
    args = parser.parse_args()

    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=args.reload,
        access_log=False,
    )