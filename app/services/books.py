import logging

from app import database, schemas

log = logging.getLogger('api')


def all_books(common) -> list[schemas.Author]:
    log.warning('service layer')
    log.warning(common)
    return database.get_all_books(common)


def add_book():
    pass
