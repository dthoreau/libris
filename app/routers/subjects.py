import logging
from fastapi import APIRouter

from app import schemas, services


from app.util import deps
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/subjects", tags=["Subjec.ts"])
def get_all_subjects(ds: deps.DataSource,
                     slice: deps.Slice) -> list[schemas.Subject]:
    return services.all_subjects(ds, slice)


@router.get("/subjects/{subject}", tags=["Subjec.ts"])
def get_subject(ds: deps.DataSource, subject: str) -> schemas.Subject:
    return services.get_subject(ds, subject)


@router.get("/subjects/{subject}/books", tags=["Subjec.ts"])
def get_subject_books(ds: deps.DataSource,
                      subject: str) -> list[schemas.Book]:
    return services.get_subject_books(ds, subject)


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
