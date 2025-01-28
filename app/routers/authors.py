import logging
from fastapi import APIRouter

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/authors", tags=["Authors"])
def get_all_authors(ds: deps.DataSource,
                    qslice: deps.Slice) -> list[schemas.Author]:
    return services.all_authors(ds, qslice)


@router.get("/authors/{author_id}", tags=["Authors"])
def get_author_by_id(ds: deps.DataSource, qslice: deps.Slice,
                     id: str) -> schemas.AuthorExtended:

    return services.get_author(ds, id, qslice)


@router.delete("/authors/{author_id}", tags=["Authors"])
def delete_author(ds: deps.DataSource, id: str) -> None:
    services.delete_author(ds, id)


@router.post("/authors", tags=["Authors"])
def create_author(ds: deps.DataSource,
                  author: schemas.AuthorCreate) -> schemas.Author:

    return services.add_author(ds, author)


@router.put("/authors/{author_id}", tags=["Authors"])
def update_author(ds: deps.DataSource, author_id: str,
                  update: schemas.AuthorCreate) -> schemas.Author:
    return services.update_author(ds, author_id, update)


@router.get("/authors/{author_id}/books", tags=["Authors"])
def get_author_books(ds: deps.DataSource, id: str,
                     qslice: deps.Slice) -> list[schemas.Book]:
    return services.get_author_books(ds, id, qslice)
