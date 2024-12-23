from typing import Optional
from pydantic import BaseModel, UUID4


class AwardBase(BaseModel):
    name: str


class AwardCreate(AwardBase):
    pass


class Award(AwardBase):
    id: UUID4


class AwardExtended(Award):
    books: Optional[list[UUID4]] = []
