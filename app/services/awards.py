import logging

from app import database, schemas

log = logging.getLogger('api')


def all_awards(common) -> list[schemas.Award]:
    return database.get_all_awards(common)
