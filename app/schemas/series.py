from pydantic import BaseModel, UUID4
from .books import SmallBook


class SeriesBase(BaseModel):
    name: str


class SeriesCreate(SeriesBase):
    pass


class Series(SeriesBase):
    id: UUID4


class SeriesExtended(Series):
    books: list[SmallBook] = []
