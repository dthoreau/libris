import logging

from app import database, schemas

log = logging.getLogger('api')


def all_subjects(common) -> list[schemas.Subject]:
    return database.get_all_subjects(common)
