import logging

from app import database, schemas

log = logging.getLogger('api')


def all_awards(common) -> list[schemas.Award]:
    return database.get_all_awards(common)


def get_award_books(common, award: str) -> list[schemas.Book]:
    return database.get_award_books(common, award_id=award)


def get_award(common, award: str) -> schemas.Award:
    return database.get_award_by_id(common, award_id=award)
