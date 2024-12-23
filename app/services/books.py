import logging

from app import database

log = logging.getLogger('api')


def get_book(common, id: str):
    return database.get_book_by_id(common, id)
