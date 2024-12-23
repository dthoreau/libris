import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/genres", tags=["Genres"])
def get_all_genres(
    common: Annotated[dict, Depends(deps.common)]) \
        -> list[schemas.Genre]:
    return services.all_genres(common)
