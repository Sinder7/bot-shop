import uvicorn

from fastapi import FastAPI

from .settings import settings
app: FastAPI = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.reload,

    )