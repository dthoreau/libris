from typing import Optional
from pydantic import BaseModel, UUID4


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: UUID4


class AuthorExtended(Author):
    books: Optional[list[UUID4]] = []
