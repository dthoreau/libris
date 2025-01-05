from typing import Optional
from pydantic import BaseModel, UUID4


class AwardBase(BaseModel):
    name: str


class AwardCreate(AwardBase):
    pass


class Award(AwardBase):
    id: UUID4


class AwardBook(BaseModel):
    id: UUID4
    title: str


class AwardExtended(Award):
    books: Optional[AwardBook] = []
