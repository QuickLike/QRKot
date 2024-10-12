from fastapi import APIRouter

from app.api.endpoints import (
    charity_project_router,
    donation_router,
    google_api_router,
    user_router
)
from app.core.config import constants

main_router = APIRouter()
main_router.include_router(
    charity_project_router,
    prefix=constants.CHARITY_PROJECT_PATH,
    tags=constants.CHARITY_PROJECT_TAGS
)
main_router.include_router(
    donation_router,
    prefix=constants.DONATION_PATH,
    tags=constants.DONATION_TAGS
)
main_router.include_router(
    google_api_router,
    prefix='/google',
    tags=['Google']
)
main_router.include_router(user_router)
