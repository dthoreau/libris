import logging

from app import database, schemas

log = logging.getLogger('api')


def all_series(ds, qslice) -> list[schemas.Series]:
    return database.get_all_series(ds, qslice)


def get_series(ds, id: str, qslice) -> schemas.SeriesExtended:
    series = database.get_series_by_id(ds, id)

    return schemas.SeriesExtended(
        name=series.name,
        id=series.id,
        books=[schemas.SmallBook(id=book.id, title=book.title)
               for book in database.get_series_books(ds, id, qslice)])


def get_series_books(ds, series: str, qslice) -> list[schemas.Book]:
    return database.get_series_books(ds, series, qslice)


def find_series(ds, name: str) -> schemas.Series:
    return database.find_series_by_name(ds, name)


def add_series(ds,
               new_series: schemas.SeriesCreate) -> schemas.Series:
    return database.add_series(ds, new_series)
