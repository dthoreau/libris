import logging

from app import database, schemas

log = logging.getLogger('api')


def all_subjects(ds, slice) -> list[schemas.Subject]:
    return database.get_all_subjects(ds, slice)


def get_subject(ds, id: str) -> schemas.Subject:
    return database.get_subject_by_id(ds, id)


def get_subject_books(ds, id: str) -> list[schemas.Book]:
    return database.get_subject_books(ds, id)


def find_subject(ds, name: str) -> schemas.Subject:
    return database.find_subject_by_name(ds, id)


def add_subject(ds,
                new_subject: schemas.SubjectCreate) -> schemas.Subject:
    return database.add_subject(ds, new_subject)
