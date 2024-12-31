from typing import Any
from sqlalchemy import Select

from app.database import get_one, get_all, insert, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_series(ds, slice) -> list[schemas.Series]:
    return get_all(
        ds,
        Select(tables.series.c.id, tables.series.c.name),
        schemas.Series,
        slice)


def get_series_books(ds: Any) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_series,
                       tables.books.c.id == tables.book_series.c.book
                  ).where(tables.book_series.c.series == id)
    return get_all(ds, query, schemas.Book)


def get_series_by_id(ds: Any, id: str) -> schemas.Series:
    query = Select(
            tables.series.c.id,
            tables.series.c.name
        ).where(tables.series.c.id == id)

    return get_one(ds, query, schemas.Series)


def add_series(ds: Any,
               new_series: schemas.SeriesCreate) -> schemas.Series:
    insert(ds, tables.series, new_series)
    return find_series_by_name(ds, new_series.name)


def find_series_by_name(ds: Any, name: str) -> schemas.Series:
    query = Select(tables.series.c.id, tables.series.c.name
                   ).where(tables.series.c.name == name)
    return get_one(ds, query, schemas.series)
