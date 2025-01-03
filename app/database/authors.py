from sqlalchemy import Select

import logging

from app import schemas
from app.database import tables, DataBase

log = logging.getLogger('api')


def get_all_authors(ds: DataBase, slice) -> list[schemas.Author]:

    stmt = Select(tables.authors.c.id, tables.authors.c.name)
    return ds.reader().get_all(stmt, schemas.Author, slice)


def get_author_by_id(ds: DataBase, id: str, slice) -> schemas.AuthorExtended:
    query = Select(
        tables.authors.c.id,
        tables.authors.c.name).where(
            tables.authors.c.id == id)

    author = ds.reader().get_one(query, schemas.AuthorExtended)

    author.books = get_author_books(ds, id, slice)

    return author


def get_author_books(ds: DataBase, id: str, slice) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_authors,
                       tables.books.c.id == tables.book_authors.c.book
                  ).where(tables.book_authors.c.author == id)
    return ds.reader().get_all(query, schemas.Book, slice)


def add_author(ds: DataBase,
               new_author: schemas.AuthorCreate) -> schemas.Author:
    ds.writer().insert(tables.authors, new_author)
    return find_author_by_name(ds, new_author.name)


def find_author_by_name(ds: DataBase, name: str) -> schemas.Author:
    query = Select(tables.authors.c.id, tables.authors.c.name
                   ).where(tables.authors.c.name == name)
    return ds.reader().get_one(query, schemas.Author)


def delete_author(ds: DataBase, author_id: int) -> None:
    ds.writer().delete(tables.authors, author_id)
