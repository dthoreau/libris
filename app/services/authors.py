import logging
from app import database, schemas

log = logging.getLogger('api')


def all_authors(datasource, slice) -> list[schemas.Author]:
    return database.get_all_authors(datasource, slice)


def get_author(datasource, id, slice: str) -> schemas.AuthorExtended:
    return database.get_author_by_id(datasource, id, slice)


def add_author(datasource,
               new_author: schemas.AuthorCreate) -> schemas.Author:
    log.info(new_author)
    return database.add_author(datasource, new_author)


def get_author_books(datasource, id: str,
                     slice) -> list[schemas.AuthorBook]:
    return database.get_author_books(datasource, id, slice)


def find_author(datasource, name: str) -> schemas.Author:
    return database.find_author_by_name(datasource, name)


def delete_author(datasource, id: str) -> None:
    database.delete_author(datasource, id)
