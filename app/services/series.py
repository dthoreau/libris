import logging

from app import database, schemas

log = logging.getLogger('api')


def all_series(ds, slice) -> list[schemas.Series]:
    return database.get_all_series(ds, slice)


def get_series(ds, id: str) -> schemas.Series:
    return database.get_series_by_id(ds, id)


def get_series_books(ds, id: str) -> list[schemas.Book]:
    return database.get_series_books(ds, id)


def find_series(ds, name: str) -> schemas.Series:
    return database.find_series_by_name(ds, name)


def add_series(ds,
               new_series: schemas.SeriesCreate) -> schemas.Series:
    return database.add_series(ds, new_series)
