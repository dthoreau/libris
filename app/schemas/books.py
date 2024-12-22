from typing import Optional
from pydantic import BaseModel, UUID4


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: str


class AuthorExtended(Author):
    books: Optional[list[int]] = []


class BookBase(BaseModel):
    title: str
    pages: Optional[str] = None
    original_isbn: Optional[str] = None
    ean: Optional[str] = None
    upc: Optional[str] = None
    asin: Optional[str] = None
    height: Optional[str] = None
    length: Optional[str] = None
    summary: Optional[str] = None
    thickness: Optional[str] = None
    page_count: Optional[str] = None
    description: Optional[str] = None
    publication: Optional[str] = None
    publication_date: Optional[str] = None


class BookPatchOptional(BaseModel):
    title: Optional[str] = None
    pages: Optional[str] = None
    original_isbn: Optional[str] = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: UUID4


class BookExtended(Book):
    author: list[UUID4] = []
    award: list[UUID4] = []


class AwardBase(BaseModel):
    name: str


class AwardCreate(AwardBase):
    pass


class Award(AwardBase):
    id: UUID4


class AwardExtended(Award):
    books: Optional[list[UUID4]] = []


class GenreBase(BaseModel):
    name: str


class Genre(GenreBase):
    id: UUID4


class SubjectBase(BaseModel):
    name: str


class Subject(SubjectBase):
    id: UUID4


class SeriesBase(BaseModel):
    name: str


class Series(SeriesBase):
    id: UUID4
