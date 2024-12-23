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
