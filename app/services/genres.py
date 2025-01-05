import logging

from app import database, schemas
from app.util import deps

log = logging.getLogger('api')


def all_genres(ds, qslice: deps.Slice) -> list[schemas.Genre]:
    return database.get_all_genres(ds, qslice)


def get_genre(ds, id: str, qslice: deps.Slice) -> schemas.Genre:
    return database.get_genre_by_id(ds, id, qslice)


def get_genre_books(ds, id: str, qslice: deps.Slice) -> list[schemas.Book]:
    return database.get_genre_books(ds, id, qslice)


def find_genre(ds, name: str) -> schemas.Genre:
    return database.find_genre_by_name(ds, name)


def add_genre(ds, new_genre: schemas.GenreCreate) -> schemas.Genre:
    return database.add_genre(ds, new_genre)
