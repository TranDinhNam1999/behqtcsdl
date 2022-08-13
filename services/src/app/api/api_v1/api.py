from app.api.api_v1.endpoints import users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(search.router, prefix="/q", tags=["queries"])
# api_router.include_router(
#     orders.router, prefix="/orders", tags=["orders"]
# )
