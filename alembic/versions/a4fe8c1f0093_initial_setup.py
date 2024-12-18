"""Initial setup

Revision ID: a4fe8c1f0093
Revises:
Create Date: 2024-12-06 15:35:45.176062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

import uuid


# revision identifiers, used by Alembic.
revision: str = 'a4fe8c1f0093'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    authors = simple_table('authors')
    awards = simple_table('awards')
    genres = simple_table('genres')
    subjects = simple_table('subjects')
    series = simple_table('series')
    
    books = op.create_table(
        'books',
        sa.Column('id', sa.UUID(as_uuid=False), primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('pages', sa.String, nullable=True),
        sa.Column('original_isbn', sa.String, nullable=True),
        sa.Column('ean', sa.String, nullable=True),
        sa.Column('upc', sa.String, nullable=True),
        sa.Column('asin', sa.String, nullable=True),
        sa.Column('height', sa.String, nullable=True),
        sa.Column('length', sa.String, nullable=True),
        sa.Column('summary', sa.String, nullable=True),
        sa.Column('thickness', sa.String, nullable=True),
        sa.Column('page_count', sa.String, nullable=True),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('publication', sa.String, nullable=True),
        sa.Column('publication_date', sa.String, nullable=True),
    )
    authorship = op.create_table(
        'authorship',
        sa.Column('book', sa.UUID, sa.ForeignKey("books.id"),
                  nullable=False),
        sa.Column('author', sa.UUID, sa.ForeignKey("authors.id"),
                  nullable=False))

    identifier_types = op.create_table(
        'identifier_types',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    author_roles = op.create_table(
        'author_roles',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    dewey_keywords = op.create_table(
        'dewey_keywords',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    identifier = op.create_table(
        'identifier',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('book', UUID(as_uuid=False),
                  sa.ForeignKey('books.id'), nullable=False),
        sa.Column('identifier)', sa.String, nullable=False),
        sa.Column('identifier_type', UUID(as_uuid=False),
                  sa.ForeignKey('identifier_types.id'), nullable=False)
    )

    book_awards = create_pivot('book_awards',
                 'book', "books.id",
                 'award', "awards.id")
    book_genre = create_pivot('book_genre',
                 'book', "books.id",
                 'genre', "genres.id")
    book_dewey = create_pivot('book_dewey',
                 'book', "books.id",
                 'dewey', "dewey_keywords.id")
    book_series = create_pivot('book_series',
                 'book', "books.id",
                 'series', "series.id")
    book_subjects = create_pivot('book_subjects',
                 'book', "books.id",
                 'subject', "subjects.id")


def downgrade() -> None:
    pass


def simple_table(table_name: str) -> None:
    table = op.create_table(
        table_name,
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    return table
                            

def create_pivot(table_name, left, left_name, right, right_name):
    table = op.create_table(
        table_name,
        sa.Column(left, sa.UUID(as_uuid=False),
                  sa.ForeignKey(left_name), nullable=False),
        sa.Column(right, sa.UUID(as_uuid=False),
                  sa.ForeignKey(right_name), nullable=False))

    return table
