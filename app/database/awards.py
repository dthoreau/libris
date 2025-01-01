from sqlalchemy import Select

from app import schemas
from app.database import tables, DataBase

import logging
logger = logging.getLogger()


def get_award_books(ds: DataBase,
                    award_id: str, slice) -> list[schemas.Book]:
    stmt = Select(tables.books.c.id, tables.books.c.title).\
        join(tables.book_awards, tables.books.c.id ==
             tables.book_awards.c.book).\
        where(tables.book_awards.c.award == award_id)
    return ds.reader().get_all(stmt, schemas.Book, slice)


def get_all_awards(ds: DataBase, slice) -> list[schemas.Award]:
    return ds.reader().get_all(
        Select(tables.awards.c.id, tables.awards.c.name),
        schemas.Award, slice)


def get_award_by_id(ds: DataBase, award_id: str) -> schemas.Award:
    stmt = Select(tables.awards.c.id, tables.awards.c.name).\
        where(tables.awards.c.id == award_id)
    return ds.reader().get_one(stmt, schemas.Award)


def add_award(ds: DataBase,
              new_award: schemas.AwardCreate) -> schemas.Award:
    ds.writer().insert(tables.awards, new_award)
    return find_award_by_name(ds, new_award.name)


def find_award_by_name(ds: DataBase, name: str) -> schemas.Award:
    query = Select(tables.awards.c.id, tables.awards.c.name
                   ).where(tables.awards.c.name == name)
    return ds.reader().get_one(query, schemas.Award)
