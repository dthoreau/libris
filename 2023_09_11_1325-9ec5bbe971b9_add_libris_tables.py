"""add libris tables

Revision ID: 9ec5bbe971b9
Revises: 296a2f52fb08
Create Date: 2023-09-11 13:25:40.293220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ec5bbe971b9'
down_revision = '296a2f52fb08'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'books',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('pages', sa.String, nullable=True),
        sa.Column('original_isbn', sa.String, nullable=True))
    op.create_table(
        'authors',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('name', sa.String, nullable=False))
    op.create_table(
        'awards',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('name', sa.String, nullable=False))

    op.create_table(
        'book_authors',
        sa.Column('book', sa.UUID, sa.ForeignKey("books.id"), nullable=False),
        sa.Column('author', sa.UUID, sa.ForeignKey("authors.id"),
                  nullable=False))
    op.create_table(
        'book_awards',
        sa.Column('book', sa.UUID, sa.ForeignKey("books.id"),
                  nullable=False),
        sa.Column('award', sa.UUID, sa.ForeignKey("awards.id"),
                  nullable=False))


def downgrade() -> None:
    libris_tables = ['book_authors', 'book_awards',
                     'books', 'awards', 'authors', ]

    for table in libris_tables:
        op.drop_table(table)
