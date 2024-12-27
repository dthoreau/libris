from typing import Any
from sqlalchemy import Select

from app.database import get_one, get_all, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_subjects(common: Any) -> list[schemas.Subject]:
    return get_all(
        common,
        Select(tables.subjects.c.id, tables.subjects.c.name),
        schemas.Subject)


def get_subject_by_id(common: Any, id: str) -> schemas.Subject:
    query = Select(tables.subjects.c.id, tables.subjects.c.name).where(
        tables.subjects.c.id == id)

    return get_one(common, query)


def get_subject_books(common: Any, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_subjects,
                       tables.books.c.id == tables.book_subjects.c.book
                  ).where(tables.book_subjects.c.book == id)
    return get_all(common, query)
