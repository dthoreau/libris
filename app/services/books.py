import logging

from app import database, schemas

log = logging.getLogger('api')


def all_authors(common) -> list[schemas.Author]:
    return database.get_all_authors(common)


def add_author(common):
    pass


def all_awards(common) -> list[schemas.Award]:
    return database.get_all_awards(common)
