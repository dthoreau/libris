from typing import Any

from sqlalchemy import Select

from app.database import get_all, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_genres(common: Any) -> list[schemas.Genre]:
    return get_all(
        common,
        Select(tables.genres.c.id, tables.genres.c.name),
        schemas.Genre
    )


def get_genre_books(common: Any, id: str) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_genres,
                       tables.books.c.id == tables.book_genres.c.book
                  ).where(tables.book_genres.c.genre == id)
    return get_all(common, query, schemas.Book)


def get_genre_by_id(common: Any, id: str) -> list[schemas.Genre]:
    query = Select(
        tables.genres.c.id, tables.genres.c.name).where(
            tables.genres.c.id == id)

    return (common, query, schemas.Genre)
