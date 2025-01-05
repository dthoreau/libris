from typing import Optional
from pydantic import BaseModel, UUID4


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: UUID4


class GenreBook(BaseModel):
    id: UUID4
    title: str


class GenreExtended(Genre):
    books: Optional[GenreBook] = []
