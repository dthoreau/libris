from typing import Any, Type, TypeVar
from pydantic import BaseModel
from sqlalchemy import (
    MetaData, Table, Column, UUID, String, ForeignKey, Select, Engine)

from app import schemas

import uuid

import logging
logger = logging.getLogger()

metadata_obj = MetaData()

ModelType = TypeVar('ModelType', bound=BaseModel)

authors = Table(
    'authors',
    metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
           default=uuid.uuid4),
    Column('name', String(), nullable=False)
)

awards = Table(
    'awards', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
           default=uuid.uuid4),
    Column('name', String(), nullable=False)
)

genres = Table(
    'genres', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
           default=uuid.uuid4),
    Column('name', String(), nullable=False)
)

subjects = Table(
    'subjects', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
           default=uuid.uuid4),
    Column('name', String(), nullable=False))

series = Table(
    'series', metadata_obj,
    Column('id', UUID(as_uuid=False), primary_key=True,
           default=uuid.uuid4),
    Column('name', String(), nullable=False)
)

book_authors = Table(
    'book_authors', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
           nullable=False),
    Column('author', UUID(as_uuid=False), ForeignKey("authors.id"),
           nullable=False))

book_awards = Table(
    'book_awards', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
           nullable=False),
    Column('award', UUID(as_uuid=False), ForeignKey("awards.id"),
           nullable=False))

books = Table(
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


def get_all_authors(common: Any) -> list[schemas.Author]:    

    stmt = Select(authors.c.id, authors.c.name)
    return _get_all(common, stmt, schemas.Author)


def get_all_awards(common: Any) -> list[schemas.Award]:
    return _get_all(
        common,
        Select(awards.c.id, awards.c.name),
        schemas.Award)


def get_all_subjects(common: Any) -> list[schemas.Subject]:
    return _get_all(
        common,
        Select(subjects.c.id, subjects.c.name),
        schemas.Subject)


def get_all_series(common: Any) -> list[schemas.Series]:
    return _get_all(
        common,
        Select(series.c.id, series.c.name),
        schemas.Series)


def get_all_genres(common: Any) -> list[schemas.Genre]:
    return _get_all(
        common,
        Select(genres.c.id, genres.c.name),
        schemas.Genre
    )


def get_all_books(common: Any) -> list[schemas.Book]:
    raise NotImplementedError


def get_book_by_id(common: Any, book_id: str) -> schemas.Book:
    query = Select(
        books.c.id,
        books.c.title,
        books.c.pages,
        books.c.original_isbn,
        books.c.ean,
        books.c.upc,
        books.c.asin,
        books.c.height,
        books.c.length,
        books.c.summary,
        books.c.thickness,
        books.c.page_count,
        books.c.description,
        books.c.publication,
        books.c.publication_date,
    ).where(books.c.id == book_id)
    return _get_one(common, query, schemas.Book)


def _get_all(common: dict[str, Any],
             query: Select,             
             model_type: Type[ModelType]) -> list[ModelType]:
    collection = []
    eng: Engine = common["eng"]
    with eng.connect() as dbh:
        logger.warning(f'{query=}')
        query = query.limit(common["limit"]).offset(common["skip"])
        for row in dbh.execute(query):
            collection.append(model_type.model_validate(row._asdict()))

        return collection

def _get_one(common: dict[str, Any],
             query: Select, 
             model_type: Type[ModelType]) -> ModelType:
    eng: Engine = common["eng"]
    with eng.connect() as dbh:
        for row in dbh.execute(query):
            return model_type.model_validate(row._asdict())
