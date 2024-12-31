from typing import Any

from sqlalchemy import Select

from . import get_one, get_all, insert

from app import schemas
from app.database import tables

import logging
logger = logging.getLogger()


def get_award_books(ds, slice, award_id: str) -> list[schemas.Book]:
    stmt = Select(tables.books.c.id, tables.books.c.title).\
        join(tables.book_awards, tables.books.c.id ==
             tables.book_awards.c.book).\
        where(tables.book_awards.c.award == award_id)
    return get_all(ds, stmt, schemas.Book, slice)


def get_all_awards(ds, slice) -> list[schemas.Award]:
    return get_all(
        ds,
        Select(tables.awards.c.id, tables.awards.c.name),
        schemas.Award, slice)


def get_award_by_id(ds: Any, award_id: str) -> schemas.Award:
    stmt = Select(tables.awards.c.id, tables.awards.c.name).\
        where(tables.awards.c.id == award_id)
    return get_one(ds, stmt, schemas.Award)


def add_award(ds: Any,
              new_award: schemas.AwardCreate) -> schemas.Award:
    insert(ds, tables.awards, new_award)
    return find_award_by_name(ds, new_award.name)


def find_award_by_name(ds: Any, name: str) -> schemas.Award:
    query = Select(tables.awards.c.id, tables.awards.c.name
                   ).where(tables.awards.c.name == name)
    return get_one(ds, query, schemas.Award)
