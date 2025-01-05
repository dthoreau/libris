from typing import Optional
from pydantic import BaseModel, UUID4


class SubjectBase(BaseModel):
    name: str


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    id: UUID4


class SubjectBook(BaseModel):
    id: UUID4
    title: str


class SubjectExtended(Subject):
    books: Optional[SubjectBook] = []
