from typing import Optional
from pydantic import BaseModel, UUID4


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: UUID4


class GenreExtended(Genre):
    books: Optional[list[UUID4]] = []
