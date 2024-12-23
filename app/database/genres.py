from typing import Any

from sqlalchemy import Select

from app.database import get_all, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_genres(common: Any) -> list[schemas.Genre]:
    return get_all(
        common,
        Select(tables.genres.c.id, tables.genres.c.name),
        schemas.Genre
    )
