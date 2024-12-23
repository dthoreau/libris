import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services


from app.util import deps

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/series", tags=["Series"])
def get_all_series(
    common: Annotated[dict, Depends(deps.common)]) -> \
        list[schemas.Series]:
    return services.all_series(common)
