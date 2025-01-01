from pydantic import BaseModel, UUID4


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: UUID4


class AuthorBook(BaseModel):
    id: UUID4
    title: str


class AuthorExtended(Author):
    books: list[AuthorBook] = []
