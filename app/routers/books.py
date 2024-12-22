import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services
from app.database import make_postgres_connection


logger = logging.getLogger(__name__)

router = APIRouter()


async def common_parameters(
        skip: int = 0, limit: int = 100):
    eng = make_postgres_connection()
    return {"skip": skip, "limit": limit, "eng": eng}


@router.get("/authors", tags=["Authors"])
def get_all_authors(
    common: Annotated[dict, Depends(common_parameters)]) \
        -> list[schemas.Author]:
    return services.all_authors(common)


@router.get("/books", tags=["Books"])
def get_all_books(
    common: Annotated[dict, Depends(common_parameters)]) \
        -> list[schemas.Book]:
    raise NotImplementedError


@router.get("/book/{id}", tags=["Books"])
def get_book(common: Annotated[dict, Depends(common_parameters)],
             id: str) -> schemas.Book:
    return services.get_book(common, id)


@router.get("/awards", tags=["Awards"])
def get_all_awards(
    common: Annotated[dict, Depends(common_parameters)]) \
        -> list[schemas.Award]:
    return services.all_awards(common)


@router.get("/genres", tags=["Genres"])
def get_all_genres(
    common: Annotated[dict, Depends(common_parameters)]) \
        -> list[schemas.Genre]:
    return services.all_genres(common)


@router.get("/subjects", tags=["Subjects"])
def get_all_subjects(
    common: Annotated[dict, Depends(common_parameters)]) -> \
        list[schemas.Subject]:
    return services.all_subjects(common)


@router.get("/series", tags=["Series"])
def get_all_series(
    common: Annotated[dict, Depends(common_parameters)]) -> \
        list[schemas.Series]:
    return services.all_series(common)
