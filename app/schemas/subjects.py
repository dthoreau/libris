from typing import Optional
from pydantic import BaseModel, UUID4


class SubjectBase(BaseModel):
    name: str


class Subject(SubjectBase):
    id: UUID4
