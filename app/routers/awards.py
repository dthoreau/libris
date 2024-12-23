import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/awards", tags=["Awards"])
def get_all_awards(
    common: Annotated[dict, Depends(deps.common)]) \
        -> list[schemas.Award]:
    return services.all_awards(common)


@router.get("/awards/{award}", tags=["Awards"])
def get_award(
    common: Annotated[dict, Depends(deps.common)], award: str) -> \
        schemas.Award:
    return services.get_award(common, award)


@router.get("/awards/{award}/books", tags=["Awards"])
def get_award_books(
    common: Annotated[dict, Depends(deps.common)], award: str) -> \
        list[schemas.Book]:
    return services.get_award_books(common, award)
