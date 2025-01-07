import logging

from app import database, schemas
from app.util import deps

log = logging.getLogger('api')


def all_awards(ds, slice) -> list[schemas.Award]:
    return database.get_all_awards(ds, slice)


def get_award_books(ds, award: str, qslice: deps.Slice) -> list[schemas.Book]:
    return database.get_award_books(ds, award, qslice)


def get_award(ds, id: str, qslice: deps.Slice) -> schemas.AwardExtended:
    award = database.get_award_by_id(ds, id)

    return schemas.AwardExtended(
        id=award.id,
        name=award.name,
        books=[schemas.SmallBook(id=book.id, title=book.title)
               for book in database.get_award_books(ds, id, qslice)])


def find_award(ds, name: str) -> schemas.Award:
    return database.find_award_by_name(ds, name)


def add_award(ds, new_award: schemas.AwardCreate) -> schemas.Award:
    return database.add_award(ds, new_award)
