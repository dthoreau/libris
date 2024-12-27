from typing import Any
from sqlalchemy import Select

from app.database import get_one, get_all, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_series(common: Any) -> list[schemas.Series]:
    return get_all(
        common,
        Select(tables.series.c.id, tables.series.c.name),
        schemas.Series)


def get_series_books(common: Any) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_series,
                       tables.books.c.id == tables.book_series.c.book
                  ).where(tables.book_series.c.book == id)
    return get_all(common, query)


def get_series_by_id(common: Any, id: str) -> schemas.Series:
    query = Select(
            tables.series.c.id,
            tables.series.c.name
        ).where(tables.series.c.id == id)

    return get_one(common, query)
