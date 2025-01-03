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
                     id: str) -> schemas.AuthorExtended:

    return services.get_author(ds, id, slice)


@router.delete("/authors/{author_id}", tags=["Authors"])
def delete_author(ds: deps.DataSource, id: str):
    services.delete_author(ds, id)


@router.post("/authors", tags=["Authors"])
def create_author(ds: deps.DataSource,
                  author: schemas.AuthorCreate) -> schemas.Author:

    return services.add_author(ds, author)


@router.put("/authors/{author_id}", tags=["Authors"])
def update_author():
    return NotImplementedError


@router.get("/authors/{author_id}/books", tags=["Authors"])
def get_author_books(ds: deps.DataSource, id: str,
                     slice: deps.Slice) -> list[schemas.AuthorBook]:
    return services.get_author_books(ds, id, slice)
