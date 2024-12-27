import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/genres", tags=["Genres"])
def get_all_genres(
    common: Annotated[dict, Depends(deps.common)]) \
        -> list[schemas.Genre]:
    return services.all_genres(common)


@router.get("/genres/{genre}", tags=["Genres"])
def get_genre(
    common: Annotated[dict, Depends(deps.common)], genre: str) -> \
        schemas.Genre:
    return services.get_genre(common, genre)


@router.get("/genres/{genre}/books", tags=["Genres"])
def get_genre_books(
    common: Annotated[dict, Depends(deps.common)], genre: str) -> \
        list[schemas.Book]:
    return services.get_genre_books(common, genre)


@router.get("/genres/{genre_id}", tags=["Genres"])
def get_genre_by_id() -> list[schemas.Genre]:
    return NotImplementedError


@router.delete("/genres/{genre_id}", tags=["Genres"])
def delete_genre():
    return NotImplementedError


@router.post("/genres", tags=["Genres"])
def create_genre():
    return NotImplementedError


@router.put("/genres/{genre_id}", tags=["Genres"])
def update_genre():
    return NotImplementedError
