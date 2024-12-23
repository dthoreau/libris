from pydantic import BaseModel, UUID4


class SeriesBase(BaseModel):
    name: str


class Series(SeriesBase):
    id: UUID4
