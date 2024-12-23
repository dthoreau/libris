from typing import Optional
from pydantic import BaseModel, UUID4


class GenreBase(BaseModel):
    name: str


class Genre(GenreBase):
    id: UUID4
