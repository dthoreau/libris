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


def add_award_to_book(ds: DataBase, book: str, award: str) -> None:
    temp_dict = {'book': book, 'award': award}
    with ds.writer() as dw:
        dw.insert(tables.book_awards, temp_dict)


def remove_award_from_book(ds: DataBase, book: str, award: str) -> None:
    pass
    with ds.writer() as dw:
        table = tables.book_awards
        stmt = Delete(table).where(
            table.c.book == book).where(table.c.award == award)

        dw.run_update_stmt(stmt)


def add_genre_to_book(ds: DataBase, book: str, genre: str) -> None:
    temp_dict = {'book': book, 'genre': genre}
    with ds.writer() as dw:
        dw.insert(tables.book_genres, temp_dict)


def remove_genre_from_book(ds: DataBase, book: str, genre: str) -> None:
    pass
    with ds.writer() as dw:
        table = tables.book_genres
        stmt = Delete(table).where(
            table.c.book == book).where(table.c.genre == genre)

        dw.run_update_stmt(stmt)


def add_series_to_book(ds: DataBase, book: str, series: str) -> None:
    temp_dict = {'book': book, 'series': series}
    with ds.writer() as dw:
        dw.insert(tables.book_series, temp_dict)


def remove_series_from_book(ds: DataBase, book: str, series: str) -> None:
    pass
    with ds.writer() as dw:
        table = tables.book_series
        stmt = Delete(table).where(
            table.c.book == book).where(table.c.series == series)

        dw.run_update_stmt(stmt)


def add_subject_to_book(ds: DataBase, book: str, subject: str) -> None:
    temp_dict = {'book': book, 'subject': subject}
    with ds.writer() as dw:
        dw.insert(tables.book_subjects, temp_dict)


def remove_subject_from_book(ds: DataBase, book: str, subject: str) -> None:
    pass
    with ds.writer() as dw:
        table = tables.book_subjects
        stmt = Delete(table).where(
            table.c.book == book).where(table.c.subjects == subject)

        dw.run_update_stmt(stmt)
