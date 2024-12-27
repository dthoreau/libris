import logging

from app import database, schemas

log = logging.getLogger('api')


def all_genres(common) -> list[schemas.Genre]:
    return database.get_all_genres(common)


def get_genre(common, id: str) -> schemas.Genre:
    return database.get_genre(common, id)


def get_genre_books(common, id: str) -> list[schemas.Book]:
    return database.get_genre_books(common, id)
