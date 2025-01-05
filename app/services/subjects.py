import logging

from app import database, schemas
from app.util import deps

log = logging.getLogger('api')


def all_subjects(ds, qslice) -> list[schemas.Subject]:
    return database.get_all_subjects(ds, qslice)


def get_subject(ds, id: str, qslice: deps.Slice) -> schemas.Subject:
    return database.get_subject_by_id(ds, id, qslice)


def get_subject_books(ds, id: str, qslice) -> list[schemas.Book]:
    return database.get_subject_books(ds, id, qslice)


def find_subject(ds, name: str) -> schemas.Subject:
    return database.find_subject_by_name(ds, name)


def add_subject(ds,
                new_subject: schemas.SubjectCreate) -> schemas.Subject:
    return database.add_subject(ds, new_subject)
