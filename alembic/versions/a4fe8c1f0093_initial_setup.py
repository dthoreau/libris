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
    simple_table('authors')
    simple_table('awards')
    simple_table('genres')
    simple_table('subjects')
    simple_table('series')

    op.create_table(
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
    op.create_table(
        'authorship',
        sa.Column('book', sa.UUID, sa.ForeignKey("books.id"),
                  nullable=False),
        sa.Column('author', sa.UUID, sa.ForeignKey("authors.id"),
                  nullable=False))

    op.create_table(
        'identifier_types',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'author_roles',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'dewey_keywords',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'identifier',
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4),
        sa.Column('book', UUID(as_uuid=False),
                  sa.ForeignKey('books.id'), nullable=False),
        sa.Column('identifier)', sa.String, nullable=False),
        sa.Column('identifier_type', UUID(as_uuid=False),
                  sa.ForeignKey('identifier_types.id'), nullable=False)
    )

    create_pivot('book_awards',
                 'book', "books.id",
                 'award', "awards.id")
    create_pivot('book_genre',
                 'book', "books.id",
                 'genre', "genres.id")
    create_pivot('book_dewey',
                 'book', "books.id",
                 'dewey', "dewey_keywords.id")
    create_pivot('book_series',
                 'book', "books.id",
                 'series', "series.id")
    create_pivot('book_subjects',
                 'book', "books.id",
                 'subject', "subjects.id")


def downgrade() -> None:
    pass


def simple_table(table_name: str) -> None:
    table = op.create_table(
        table_name,
        sa.Column('id', UUID(as_uuid=False), primary_key=True,
                  default=uuid.uuid4, unique=True),
        sa.Column('name', sa.String(), nullable=False, unique=True)
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
