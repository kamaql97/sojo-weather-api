from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    status_code=HTTPStatus.OK,
    tags=["Health Check"],
)
def get_health_status():
    return "OK"
