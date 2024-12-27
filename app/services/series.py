import logging

from app import database, schemas

log = logging.getLogger('api')


def all_series(common) -> list[schemas.Series]:
    return database.get_all_series(common)


def get_series(common, id: str) -> schemas.Series:
    return database.get_series_by_id(common, id)


def get_series_books(common, id: str) -> list[schemas.Book]:
    return database.get_series_books(common, id)
