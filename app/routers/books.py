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


@router.get("/books", tags=["Books"])
def get_all_books(
    common: Annotated[dict, Depends(common_parameters)]) \
        -> list[schemas.Book]:
    raise NotImplementedError


@router.get("/book/{id}", tags=["Books"])
def get_book(common: Annotated[dict, Depends(common_parameters)],
             id: str) -> schemas.BookDetail:
    return services.get_book(common, id)
