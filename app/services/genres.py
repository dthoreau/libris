import logging

from app import database, schemas

log = logging.getLogger('api')


def all_genres(common) -> list[schemas.Genre]:
    return database.get_all_genres(common)
