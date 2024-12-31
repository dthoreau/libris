from sqlalchemy import Select
from typing import Any

from . import get_all, get_one, insert

from app import schemas
from app.database import tables


def get_all_authors(ds, slice) -> list[schemas.Author]:

    stmt = Select(tables.authors.c.id, tables.authors.c.name)
    return get_all(ds, stmt, schemas.Author, slice)


def get_author_by_id(ds: Any, id: str) -> schemas.Author:
    query = Select(
        tables.authors.c.id,
        tables.authors.c.name).where(
            tables.authors.id == id)

    return get_one(ds, query, schemas.Author)


def get_author_books(ds, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_authors,
                       tables.books.c.id == tables.book_authors.c.book
                  ).where(tables.book_authors.c.author == id)
    return get_all(ds, query, schemas.Book)


def add_author(ds,
               new_author: schemas.AuthorCreate) -> schemas.Author:
    insert(ds, tables.authors, new_author)
    return find_author_by_name(ds, new_author.name)


def find_author_by_name(ds, name: str) -> schemas.Author:
    query = Select(tables.authors.c.id, tables.authors.c.name
                   ).where(tables.authors.c.name == name)
    return get_one(ds, query, schemas.Author)
