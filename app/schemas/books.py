from typing import Optional
from pydantic import BaseModel, UUID4


class BookBase(BaseModel):
    title: str
    pages: Optional[str] = None
    original_isbn: Optional[str] = None
    ean: Optional[str] = None
    upc: Optional[str] = None
    asin: Optional[str] = None
    height: Optional[str] = None
    length: Optional[str] = None
    summary: Optional[str] = None
    thickness: Optional[str] = None
    page_count: Optional[str] = None
    description: Optional[str] = None
    publication: Optional[str] = None
    publication_date: Optional[str] = None


class BookPatchOptional(BaseModel):
    title: Optional[str] = None
    pages: Optional[str] = None
    original_isbn: Optional[str] = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: UUID4


class BookExtended(Book):
    author: list[UUID4] = []
    award: list[UUID4] = []
