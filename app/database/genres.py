from sqlalchemy import Select

from app.database import tables, DataBase
from app import schemas
from app.util import deps

import logging
logger = logging.getLogger()


def get_all_genres(ds: DataBase,
                   qslice: deps.Slice) -> list[schemas.Genre]:
    return ds.reader().get_all(
        Select(tables.genres.c.id, tables.genres.c.name),
        schemas.Genre,
        qslice
    )


def get_genre_books(ds: DataBase,
                    id: str, qslice: deps.Slice) -> list[schemas.Book]:
    query = Select(tables.books.c.id,
                   tables.books.c.title
                   ).join(
                       tables.book_genres,
                       tables.books.c.id == tables.book_genres.c.book
                  ).where(tables.book_genres.c.genre == id)
    return ds.reader().get_all(query, schemas.Book, qslice)


def get_genre_by_id(ds: DataBase, id: str,
                    qslice: deps.Slice) -> schemas.GenreExtended:
    query = Select(
        tables.genres.c.id, tables.genres.c.name).where(
            tables.genres.c.id == id)

    genre = ds.reader().get_one(query, schemas.GenreExtended)
    genre.books = get_genre_books(ds, id, qslice)

    return genre


def add_genre(ds: DataBase,
              new_genre: schemas.GenreCreate) -> schemas.Genre:
    with ds.writer() as dw:
        dw.insert(tables.genres, new_genre)
    return find_genre_by_name(ds, new_genre.name)


def find_genre_by_name(ds: DataBase, name: str) -> schemas.Genre:
    query = Select(tables.genres.c.id, tables.genres.c.name
                   ).where(tables.genres.c.name == name)
    return ds.reader().get_one(query, schemas.Genre)
