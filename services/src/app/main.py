import time

from app.api.api_v1.api import api_router
from app.core.config import settings, setup_app_logging
from app.error.error_handlers import add_app_exception_handlers
from fastapi import APIRouter, FastAPI, Request

root_router = APIRouter()

app = FastAPI(
    title=settings.API_NAME, openapi_url=f"{settings.API_V1_STR}/{settings.API_DOC}"
)

setup_app_logging(config=settings)
add_app_exception_handlers(app)


@root_router.get("/ping", status_code=200, tags=["health-check"])
async def health_check():
    return {"message": "pong"}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)
