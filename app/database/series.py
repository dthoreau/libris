from sqlalchemy import Select

from app.database import tables, DataBase
from app import schemas

import logging
logger = logging.getLogger()


def get_all_series(ds: DataBase, slice) -> list[schemas.Series]:
    return ds.get_all(
        Select(tables.series.c.id, tables.series.c.name),
        schemas.Series,
        slice)


def get_series_books(ds: DataBase, slice) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_series,
                       tables.books.c.id == tables.book_series.c.book
                  ).where(tables.book_series.c.series == id)
    return ds.get_all(query, schemas.Book, slice)


def get_series_by_id(ds: DataBase, id: str) -> schemas.Series:
    query = Select(
            tables.series.c.id,
            tables.series.c.name
        ).where(tables.series.c.id == id)

    return ds.get_one(query, schemas.Series)


def add_series(ds: DataBase,
               new_series: schemas.SeriesCreate) -> schemas.Series:
    ds.insert(tables.series, new_series)
    return find_series_by_name(new_series.name)


def find_series_by_name(ds: DataBase, name: str) -> schemas.Series:
    query = Select(tables.series.c.id, tables.series.c.name
                   ).where(tables.series.c.name == name)
    return ds.get_one(query, schemas.series)
