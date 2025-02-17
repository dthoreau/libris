from starlette_admin.contrib.sqla import Admin, ModelView
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from app.util import ExtendModelView, deps
from app import database

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


class Award(Base):
    __tablename__ = 'awards'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


class Series(Base):
    __tablename__ = 'series'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


class Genre(Base):
    __tablename__ = 'genres'
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


def setup_admin(admin: Admin, ds: deps.DataBase) -> None:
    admin.add_view(ExtendModelView(
        ds, 'author', name='Author', label='Authors',
        icon='fa-regular fa-user', want_fields=('id', 'name'),
        table=database.tables.authors))

    admin.add_view(ModelView(Award, icon='faa-regular fa-star'))
    admin.add_view(ModelView(Genre, icon='fas fa-list'))
    admin.add_view(ModelView(Series, icon='fas fa-list',
                             label='Series'))
    admin.add_view(ModelView(Subject, icon='fas fa-list'))

    admin.add_view(ExtendModelView(
        ds, 'book', name='Book',
        label='Books', icon='fa-regular fa-book',
        want_fields=('id', 'title'), table=database.tables.books))
