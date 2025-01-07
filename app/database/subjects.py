from sqlalchemy import Select

from app.database import tables, DataBase
from app import schemas
from app.util import deps

import logging
logger = logging.getLogger()


def get_all_subjects(ds: DataBase,
                     qslice: deps.Slice) -> list[schemas.Subject]:
    return ds.reader().get_all(
        Select(tables.subjects.c.id, tables.subjects.c.name),
        schemas.Subject, slice=qslice)


def get_subject_by_id(ds: DataBase, id: str,
                      qslice: deps.Slice) -> schemas.Subject:
    query = Select(tables.subjects.c.id, tables.subjects.c.name).where(
        tables.subjects.c.id == id)

    return ds.reader().get_one(query, schemas.Subject)


def get_subject_books(ds: DataBase, id: str,
                      qslice: deps.Slice) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_subjects,
                       tables.books.c.id == tables.book_subjects.c.book
                  ).where(tables.book_subjects.c.subject == id)
    return ds.reader().get_all(query, schemas.Book, qslice)


def add_subject(ds: DataBase,
                new_subject: schemas.SubjectCreate) -> schemas.Subject:
    with ds.writer() as dw:
        dw.insert(tables.subjects, new_subject)
    return find_subject_by_name(new_subject.name)


def find_subject_by_name(ds: DataBase, name: str) -> schemas.Subject:
    query = Select(tables.subjects.c.id, tables.subjects.c.name
                   ).where(tables.subjects.c.name == name)
    return ds.reader().get_one(query, schemas.Subject)
