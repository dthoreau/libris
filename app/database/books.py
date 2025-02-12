from sqlalchemy import Select

from app.database import tables, DataBase
from app import schemas

from sqlalchemy import Delete

import logging
logger = logging.getLogger()


def get_all_books(ds: DataBase, slice) -> list[schemas.Book]:
    query = Select(tables.books.c.id, tables.books.c.title)
    return ds.reader().get_all(query, schemas.Book, slice)


def get_book_by_id(ds: DataBase, book_id: str) -> schemas.BookDetail:
    query = Select(
        tables.books.c.id,
        tables.books.c.title,
        tables.books.c.pages,
        tables.books.c.original_isbn,
        tables.books.c.ean,
        tables.books.c.upc,
        tables.books.c.asin,
        tables.books.c.height,
        tables.books.c.length,
        tables.books.c.summary,
        tables.books.c.thickness,
        tables.books.c.page_count,
        tables.books.c.description,
        tables.books.c.publication,
        tables.books.c.publication_date,
    ).where(tables.books.c.id == book_id)
    return ds.reader().get_one(query, schemas.Book)


def add_author_to_book(ds: DataBase, book: str, author: str) -> None:
    temp_dict = {'book': book, 'author': author}
    with ds.writer() as dw:
        dw.insert(tables.book_authors, temp_dict)


def remove_author_from_book(ds: DataBase, book: str,
                            author: str) -> None:
    with ds.writer() as dw:
        table = tables.book_authors
        stmt = Delete(table).where(
            table.c.book == book).where(table.c.author == author)

        dw.run_update_stmt(stmt)
    pass
