from typing import Optional
from pydantic import BaseModel, UUID4


class SeriesBase(BaseModel):
    name: str


class SeriesCreate(SeriesBase):
    pass


class Series(SeriesBase):
    id: UUID4


class SeriesBook(BaseModel):
    id: UUID4
    title: str


class SeriesExtended(Series):
    books: Optional[SeriesBook] = []
