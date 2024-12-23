import logging

from app import database, schemas

log = logging.getLogger('api')


def all_series(common) -> list[schemas.Series]:
    return database.get_all_series(common)
