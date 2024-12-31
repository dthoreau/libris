import logging

from app import database, schemas

log = logging.getLogger('api')


def all_genres(ds, slice) -> list[schemas.Genre]:
    return database.get_all_genres(ds, slice)


def get_genre(ds, id: str) -> schemas.Genre:
    return database.get_genre_by_id(ds, id)


def get_genre_books(ds, id: str) -> list[schemas.Book]:
    return database.get_genre_books(ds, id)


def find_genre(ds, name: str) -> schemas.Genre:
    return database.find_genre_by_name(ds, name)


def add_genre(ds, new_genre: schemas.GenreCreate) -> schemas.Genre:
    return database.add_genre(ds, new_genre)
