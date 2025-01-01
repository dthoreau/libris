import logging
from app import database, schemas

log = logging.getLogger('api')


def all_authors(datasource, slice) -> list[schemas.Author]:
    return database.get_all_authors(datasource, slice)


def get_author(datasource, slice, id: str) -> schemas.Author:
    return database.get_author_by_id(datasource, slice, id)


def add_author(datasource,
               new_author: schemas.AuthorCreate) -> None:
    log.info(new_author)
    return database.add_author(datasource, new_author)


def find_author(datasource, name: str) -> schemas.Author:
    return database.find_author_by_name(datasource, name)
