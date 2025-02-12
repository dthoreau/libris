import logging

from app import database, schemas
from app.util import deps

log = logging.getLogger('api')


def get_book(ds, id: str) -> schemas.BookDetail:
    return database.get_book_by_id(ds, id)


def all_books(ds, qslice: deps.Slice) -> list[schemas.Book]:
    return database.get_all_books(ds, qslice)


def add_author_to_book(ds, id: str, author: str) -> None:
    database.add_author_to_book(ds, id, author)


def remove_author_from_book(ds, id: str, author: str) -> None:
    database.remove_author_from_book(ds, id, author)
