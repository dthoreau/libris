from typing import Any
from sqlalchemy import Select

from database import get_all, tables
from app import schemas

import logging
logger = logging.getLogger()


def get_all_subjects(common: Any) -> list[schemas.Subject]:
    return get_all(
        common,
        Select(tables.subjects.c.id, tables.subjects.c.name),
        schemas.Subject)
