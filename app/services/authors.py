import logging
from app import database, schemas

log = logging.getLogger('api')


def all_authors(common) -> list[schemas.Author]:
    return database.get_all_authors(common)


def get_author(common, id: str) -> schemas.Author:
    return database.get_author_by_id(common, id)


def add_author(common, 
               new_author: schemas.AuthorCreate) -> None:
    return database.add_author(common, new_author)           
