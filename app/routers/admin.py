from starlette_admin.contrib.sqla import Admin, ModelView
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

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


def setup_admin(admin: Admin):
    admin.add_view(ModelView(Author, icon='fa-regular fa-user'))
    admin.add_view(ModelView(Award, icon='faa-regular fa-star'))
    admin.add_view(ModelView(Series, icon='fas fa-list'))
    admin.add_view(ModelView(Subject, icon='fas fa-list'))
    admin.add_view(ModelView(Genre, icon='fas fa-list'))
