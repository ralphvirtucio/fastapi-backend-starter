from fastapi import APIRouter

from app.api.routes import utils
from app.api.routes import users


api_router = APIRouter()
api_router.include_router(utils.router)
api_router.include_router(users.router)
