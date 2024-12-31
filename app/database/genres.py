from typing import Any

from sqlalchemy import Select

from app.database import get_all, tables, get_one, insert
from app import schemas

import logging
logger = logging.getLogger()


def get_all_genres(ds, slice) -> list[schemas.Genre]:
    return get_all(
        ds,
        Select(tables.genres.c.id, tables.genres.c.name),
        schemas.Genre,
        slice
    )


def get_genre_books(ds, slice, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_genres,
                       tables.books.c.id == tables.book_genres.c.book
                  ).where(tables.book_genres.c.genre == id)
    return get_all(ds, query, schemas.Book, slice)


def get_genre_by_id(ds: Any, id: str) -> list[schemas.Genre]:
    query = Select(
        tables.genres.c.id, tables.genres.c.name).where(
            tables.genres.c.id == id)

    return get_one(ds, query, schemas.Genre)


def add_genre(ds: Any,
              new_genre: schemas.GenreCreate) -> schemas.Genre:
    insert(ds, tables.genres, new_genre)
    return find_genre_by_name(ds, new_genre.name)


def find_genre_by_name(ds: Any, name: str) -> schemas.Genre:
    query = Select(tables.genres.c.id, tables.genres.c.name
                   ).where(tables.genres.c.name == name)
    return get_one(ds, query, schemas.Genre)
