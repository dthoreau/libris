import logging

from app import database, schemas

log = logging.getLogger('api')


def all_awards(ds, slice) -> list[schemas.Award]:
    return database.get_all_awards(ds, slice)


def get_award_books(ds, award: str, slice) -> list[schemas.Book]:
    return database.get_award_books(ds, award_id=award, slice=slice)


def get_award(ds, award: str, slice) -> schemas.Award:
    return database.get_award_by_id(ds, award_id=award)


def find_award(ds, name: str) -> schemas.Award:
    return database.find_award_by_name(ds, name)


def add_award(ds, new_award: schemas.AwardCreate) -> schemas.Award:
    return database.add_award(ds, new_award)
