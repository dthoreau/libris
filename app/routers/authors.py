import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/authors", tags=["Authors"])
def get_all_authors(
    common: Annotated[dict, Depends(deps.common)]) \
        -> list[schemas.Author]:
    return services.all_authors(common)


@router.get("/authors/{author_id}", tags=["Authors"])
def get_author_by_id(
        common: Annotated[dict, Depends(deps.common)],
        id: str) -> list[schemas.Author]:

    return services.get_author(common, id)


@router.delete("/authors/{author_id}", tags=["Authors"])
def delete_author():
    return NotImplementedError


@router.post("/authors", tags=["Authors"])
def create_author(common: Annotated[dict, Depends(deps.common)],
                  author: schemas.AuthorCreate):

    return services.add_author(common, author)


@router.put("/authors/{author_id}", tags=["Authors"])
def update_author():
    return NotImplementedError
