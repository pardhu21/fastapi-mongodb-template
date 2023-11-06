from fastapi import APIRouter

from app.api.api_v1.test.route import test_router


api_router = APIRouter()
api_router.include_router(test_router)