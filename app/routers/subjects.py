import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services


from app.util import deps
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/subjects", tags=["Subjects"])
def get_all_subjects(
    common: Annotated[dict, Depends(deps.common)]) -> \
        list[schemas.Subject]:
    return services.all_subjects(common)
