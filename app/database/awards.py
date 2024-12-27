from typing import Any

from sqlalchemy import Select

from . import get_one, get_all

from app import schemas
from app.database import tables

import logging
logger = logging.getLogger()


def get_award_books(common: Any, award_id: str) -> list[schemas.Book]:
    stmt = Select(tables.books.c.id, tables.books.c.title).\
        join(tables.book_awards, tables.books.c.id ==
             tables.book_awards.c.book).\
        where(tables.book_awards.c.award == award_id)
    return get_all(common, stmt, schemas.Book)


def get_all_awards(common: Any) -> list[schemas.Award]:
    return get_all(
        common,
        Select(tables.awards.c.id, tables.awards.c.name),
        schemas.Award)


def get_award_by_id(common: Any, award_id: str) -> schemas.Award:
    stmt = Select(tables.awards.c.id, tables.awards.c.name).\
        where(tables.awards.c.id == award_id)
    return get_one(common, stmt, schemas.Award)
