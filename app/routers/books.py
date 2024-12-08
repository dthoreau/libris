import logging
from fastapi import APIRouter

from app import schemas, services


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/books", tags=["Books"])
def get_all_books() -> list[schemas.books.Author]:
    return services.all_books()
