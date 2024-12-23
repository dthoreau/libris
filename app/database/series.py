from typing import Any
from sqlalchemy import Select

from app.database import get_all, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_series(common: Any) -> list[schemas.Series]:
    return get_all(
        common,
        Select(tables.series.c.id, tables.series.c.name),
        schemas.Series)
