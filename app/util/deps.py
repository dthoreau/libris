import logging
from app.database import DataBase

from typing import Annotated
from fastapi import Depends

logger = logging.getLogger(__name__)

SliceDep = Annotated[dict, Depends(slice)]


class QuerySlice(object):
    skip: int
    limit: int

    def __init__(self, skip: int, limit: int):
        self.skip = skip
        self.limit = limit


async def slice(skip: int = 0, limit: int = 100):
    return QuerySlice(skip, limit)


async def database():
    return DataBase()

Slice = Annotated[dict, Depends(slice)]
DataSource = Annotated[dict, Depends(database)]
