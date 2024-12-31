from typing import Any
from sqlalchemy import Select

from app.database import get_one, get_all, insert, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_subjects(ds, slice) -> list[schemas.Subject]:
    return get_all(
        ds,
        Select(tables.subjects.c.id, tables.subjects.c.name),
        schemas.Subject, slice=slice)


def get_subject_by_id(ds: Any, id: str) -> schemas.Subject:
    query = Select(tables.subjects.c.id, tables.subjects.c.name).where(
        tables.subjects.c.id == id)

    return get_one(ds, query, schemas.Subject)


def get_subject_books(ds, slice, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_subjects,
                       tables.books.c.id == tables.book_subjects.c.book
                  ).where(tables.book_subjects.c.subject == id)
    return get_all(ds, query, schemas.Book, slice)


def add_subject(ds: Any,
                new_subject: schemas.SubjectCreate) -> schemas.Subject:
    insert(ds, tables.subjects, new_subject)
    return find_subject_by_name(ds, new_subject.name)


def find_subject_by_name(ds: Any, name: str) -> schemas.Subject:
    query = Select(tables.subjects.c.id, tables.subjects.c.name
                   ).where(tables.subjects.c.name == name)
    return get_one(ds, query, schemas.Subject)
