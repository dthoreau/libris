import logging

from fastapi import APIRouter

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/books", tags=["Books"])
def get_all_books(ds: deps.DataSource,
                  slice: deps.Slice) -> list[schemas.Book]:
    return services.all_books(ds, slice)


@router.get("/book/{id}", tags=["Books"])
def get_book(ds: deps.DataSource, id: str) -> schemas.BookDetail:
    return services.get_book(ds, id)
