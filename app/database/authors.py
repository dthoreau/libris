from sqlalchemy import Select
from typing import Any

from . import get_all

from app import schemas
from app.database import tables


def get_all_authors(common: Any) -> list[schemas.Author]:

    stmt = Select(tables.authors.c.id, tables.authors.c.name)
    return get_all(common, stmt, schemas.Author)
