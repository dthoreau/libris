from typing import Any
from sqlalchemy import (
    MetaData, Table, Column, UUID, String, ForeignKey, Select,
    Connection)

from . import make_postgres_connection

from app import schemas

import uuid

import logging
logger = logging.getLogger()

metadata_obj = MetaData()


authors = Table(
    'authors',
    metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
            default=uuid.uuid4),
    Column('name', String(), nullable=False)
)

Table(
    'award', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
            default=uuid.uuid4),
    Column('name', String(), nullable=False)
)
Table(
    'genres', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
            default=uuid.uuid4),
    Column('name', String(), nullable=False)
)

Table(
    'subjects', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
            default=uuid.uuid4),
    Column('name', String(), nullable=False))

Table(
    'book_authors', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
            nullable=False),
    Column('author', UUID(as_uuid=False), ForeignKey("authors.id"),
            nullable=False))

Table(
    'book_awards', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
            nullable=False),
    Column('award', UUID(as_uuid=False), ForeignKey("awards.id"),
            nullable=False))

Table(
    'books',
    metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True),
    Column('title', String(), nullable=False),
    Column('pages', String(), nullable=True),
    Column('original_isbn', String(), nullable=True),
    Column('ean', String(), nullable=True),
    Column('upc', String(), nullable=True),
    Column('asin', String(), nullable=True),
    Column('height', String(), nullable=True),
    Column('length', String(), nullable=True),
    Column('summary', String(), nullable=True),
    Column('thickness', String(), nullable=True),
    Column('page_count', String(), nullable=True),
    Column('description', String(), nullable=True),
    Column('publication', String(), nullable=True),
    Column('publication_date', String(), nullable=True),
)
    


def get_all_books(common: Any) -> list[schemas.Author]:
    logger.warning(metadata_obj)
    eng = make_postgres_connection()

    stmt = Select(authors.c.id, authors.c.name)
    collection = []
    with  eng.connect() as dbh:
        logger.warning(f'{stmt=}')
        for row in dbh.execute(stmt):
            logger.warning(row)
            
            collection.append(row)

        return collection
