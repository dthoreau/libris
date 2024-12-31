from sqlalchemy import Select
from typing import Any

from . import get_all, get_one, insert

from app import schemas
from app.database import tables


def get_all_authors(common: Any) -> list[schemas.Author]:

    stmt = Select(tables.authors.c.id, tables.authors.c.name)
    return get_all(common, stmt, schemas.Author)


def get_author_by_id(common: Any, id: str) -> schemas.Author:
    query = Select(
        tables.authors.c.id,
        tables.authors.c.name).where(
            tables.authors.id == id)

    return get_one(common, query, schemas.Author)


def get_author_books(common, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_authors,
                       tables.books.c.id == tables.book_authors.c.book
                  ).where(tables.book_authors.c.author == id)
    return get_all(common, query, schemas.Book)

def add_author(common, 
               new_author: schemas.AuthorCreate) -> schemas.Author:
    insert(common, tables.authors, new_author)
    return find_author_by_name(common, new_author.name)
    

def find_author_by_name(common, name: str) -> schemas.Author:
    query = Select(tables.authors.c.id, tables.authors.c.name
                   ).where(tables.authors.c.name == name)
    return get_one(common, query, schemas.Author)
