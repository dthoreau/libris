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


def add_award_to_book(ds, id: str, award: str) -> None:
    database.add_award_to_book(ds, id, award)


def remove_award_from_book(ds, id: str, award: str) -> None:
    database.remove_award_from_book(ds, id, award)


def add_genre_to_book(ds, id: str, genre: str) -> None:
    database.add_genre_to_book(ds, id, genre)


def remove_genre_to_book(ds, id: str, genre: str) -> None:
    database.remove_genre_from_book(ds, id, genre)


def add_series_to_book(ds, id: str, series: str) -> None:
    database.add_series_to_book(ds, id, series)


def remove_series_from_book(ds, id: str, series: str) -> None:
    database.remove_series_from_book(ds, id, series)


def add_subject_to_book(ds, id: str, subject: str) -> None:
    database.add_subject_to_book(ds, id, subject)


def remove_subject_from_book(ds, id: str, subject: str) -> None:
    database.remove_subject_from_book(ds, id, subject)
