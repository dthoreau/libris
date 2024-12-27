import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services


from app.util import deps
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/subjects", tags=["Subjec.ts"])
def get_all_subjects(
    common: Annotated[dict, Depends(deps.common)]) -> \
        list[schemas.Subject]:
    return services.all_subjects(common)


@router.get("/subjects/{subject}", tags=["Subjec.ts"])
def get_subject(
    common: Annotated[dict, Depends(deps.common)], subject: str) -> \
        schemas.Subject:
    return services.get_subject(common, subject)


@router.get("/subjects/{subject}/books", tags=["Subjec.ts"])
def get_subject_books(
    common: Annotated[dict, Depends(deps.common)], subject: str) -> \
        list[schemas.Book]:
    return services.get_subject_books(common, subject)


@router.get("/subjects/{subject_id}", tags=["Subjec.ts"])
def get_subject_by_id():
    return NotImplementedError


@router.delete("/subjects/{subject_id}", tags=["Subjec.ts"])
def delete_subject():
    return NotImplementedError


@router.post("/subjects", tags=["Subjec.ts"])
def create_subject():
    return NotImplementedError


@router.put("/subjects/{subject_id}", tags=["Subjec.ts"])
def update_subject():
    return NotImplementedError
