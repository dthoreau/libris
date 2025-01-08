import logging
from app import database, schemas

log = logging.getLogger('api')


def all_authors(datasource, slice) -> list[schemas.Author]:
    return database.get_all_authors(datasource, slice)


def get_author(datasource, id, qslice) -> schemas.AuthorExtended:
    author = database.get_author_by_id(datasource, id)

    return schemas.AuthorExtended(
        name=author.name,
        id=author.id,
        books=[schemas.SmallBook(id=book.id, title=book.title) for book
               in database.get_author_books(datasource, id, qslice)])


def add_author(datasource,
               new_author: schemas.AuthorCreate) -> schemas.Author:
    log.info(new_author)
    return database.add_author(datasource, new_author)


def get_author_books(datasource, id: str,
                     slice) -> list[schemas.Book]:
    return database.get_author_books(datasource, id, slice)


def find_author(datasource, name: str) -> schemas.Author:
    return database.find_author_by_name(datasource, name)


def delete_author(datasource, id: str) -> None:
    database.delete_author(datasource, id)


def update_author(ds: database.DataBase, author_id, update) -> schemas.Author:
    with ds.writer() as dw:
        database.update_author(dw, author_id, update)

    return database.get_author_by_id(ds, author_id)
