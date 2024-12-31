from typing import TypeVar
from pydantic import BaseModel
from sqlalchemy import (
    MetaData, Table, Column, UUID, String, ForeignKey)

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

book_series = Table(
    'book_series', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
           nullable=False),
    Column('serues', UUID(as_uuid=False), ForeignKey("series.id"),
           nullable=False))

book_subjects = Table(
    'book_subject', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
           nullable=False),
    Column('subject', UUID(as_uuid=False), ForeignKey("subject.id"),
           nullable=False))

book_genres = Table(
    'book_genre', metadata_obj,
    Column('book', UUID(as_uuid=False), ForeignKey("books.id"),
           nullable=False),
    Column('genre', UUID(as_uuid=False), ForeignKey("genres.id"),
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
