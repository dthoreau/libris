import logging

from app import database
from app import schemas

log = logging.getLogger('api')


def get_book(common, id: str) -> schemas.BookDetail:
    return database.get_book_by_id(common, id)


def all_books(common) -> list[schemas.Book]:
    return database.get_all_books(common)
