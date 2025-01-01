from sqlalchemy import Select

from app import schemas
from app.database import tables, DataBase


def get_all_authors(ds: DataBase, slice) -> list[schemas.Author]:

    stmt = Select(tables.authors.c.id, tables.authors.c.name)
    return ds.get_all(stmt, schemas.Author, slice)


def get_author_by_id(ds: DataBase, id: str) -> schemas.Author:
    query = Select(
        tables.authors.c.id,
        tables.authors.c.name).where(
            tables.authors.id == id)

    return ds.get_one(query, schemas.Author)


def get_author_books(ds: DataBase, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_authors,
                       tables.books.c.id == tables.book_authors.c.book
                  ).where(tables.book_authors.c.author == id)
    return ds.get_all(query, schemas.Book)


def add_author(ds: DataBase,
               new_author: schemas.AuthorCreate) -> schemas.Author:
    ds.insert(tables.authors, new_author)
    return find_author_by_name(ds, new_author.name)


def find_author_by_name(ds: DataBase, name: str) -> schemas.Author:
    query = Select(tables.authors.c.id, tables.authors.c.name
                   ).where(tables.authors.c.name == name)
    return ds.get_one(query, schemas.Author)
