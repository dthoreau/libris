import logging

from app import database, schemas

log = logging.getLogger('api')


def all_subjects(common) -> list[schemas.Subject]:
    return database.get_all_subjects(common)


def get_subject(common, id: str) -> schemas.Subject:
    return database.get_subject_by_id(common, id)


def get_subject_books(common, id: str) -> list[schemas.Book]:
    return database.get_subject_books(common, id)
