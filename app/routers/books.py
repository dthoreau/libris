import logging
from fastapi import APIRouter

from . import schemas

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/books", tags=["Books"])
def get_all_books() -> schemas.books.Book:
    return [{"username": "Rick"}, {"username": "Morty"}]
