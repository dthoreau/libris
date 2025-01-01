import logging
from fastapi import APIRouter

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/authors", tags=["Authors"])
def get_all_authors(ds: deps.DataSource,
                    slice: deps.Slice) -> list[schemas.Author]:

    return services.all_authors(ds, slice)


@router.get("/authors/{author_id}", tags=["Authors"])
def get_author_by_id(ds: deps.DataSource, slice: deps.Slice,
                     id: str) -> list[schemas.Author]:

    return services.get_author(ds, slice, id)


@router.delete("/authors/{author_id}", tags=["Authors"])
def delete_author():
    return NotImplementedError


@router.post("/authors", tags=["Authors"])
def create_author(ds: deps.DataSource,
                  author: schemas.AuthorCreate) -> schemas.Author:

    return services.add_author(ds, author)


@router.put("/authors/{author_id}", tags=["Authors"])
def update_author():
    return NotImplementedError
