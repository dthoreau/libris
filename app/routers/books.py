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


# Pivot manipulators
@router.post("/book/{id}/author/{author}", tags=['Books', 'Authors'])
def add_author_to_book(ds: deps.DataSource, id: str, author: str) -> None:
    services.add_author_to_book(ds, id, author)


@router.delete("/book/{id}/author/{author}", tags=['Books', 'Authors'])
def remove_author_from_book(ds: deps.DataSource,
                            id: str, author: str) -> None:
    services.remove_author_from_book(ds, id, author)


@router.post("/book/{id}/award/{award}", tags=['Books', 'Awards'])
def add_award_to_book(ds: deps.DataSource, id: str, author: str) -> None:
    services.add_award_to_book(ds, id, author)


@router.delete("/book/{id}/award/{award}", tags=['Books', 'Awards'])
def remove_award_from_book(ds: deps.DataSource, id: str,
                           award: str) -> None:
    services.remove_award_from_book(ds, id, award)


@router.post("/book/{id}/genre/{genre}", tags=['Books', 'Genres'])
def add_genre_to_book(ds: deps.DataSource, id: str,
                      genre: str) -> None:
    services.add_genre_to_book(ds, id, genre)


@router.delete("/book/{id}/genre/{genre}", tags=['Books', 'Genres'])
def remove_genre_from_book(ds: deps.DataSource,
                           id: str, genre: str) -> None:
    services.remove_genre_from_book(ds, id, genre)


@router.post("/book/{id}/series/{series}", tags=['Books', 'Series'])
def add_series_to_book(ds: deps.DataSource, id: str, series: str) -> None:
    services.add_series_to_book(ds, id, series)


@router.delete("/book/{id}/series/{series}", tags=['Books', 'Series'])
def remove_series_from_book(ds: deps.DataSource,
                            id: str, series: str) -> None:
    services.remove_series_from_book(ds, id, series)


@router.post("/book/{id}/author/{subject}", tags=['Books', 'Subjects'])
def add_subject_to_book(ds: deps.DataSource, id: str,
                        subject: str) -> None:
    services.add_subject_to_book(ds, id, subject)


@router.delete("/book/{id}/subject/{subject}", tags=['Books', 'Subjects'])
def remove_subject_from_book(ds: deps.DataSource,
                             id: str, subject: str) -> None:
    services.remove_subject_from_book(ds, id, subject)
