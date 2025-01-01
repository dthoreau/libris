import logging
from app.database import DataBase

from typing import Annotated
from fastapi import Depends

logger = logging.getLogger(__name__)

SliceDep = Annotated[dict, Depends(slice)]


async def slice(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}


async def database():
    return DataBase()

Slice = Annotated[dict, Depends(slice)]
DataSource = Annotated[dict, Depends(database)]
