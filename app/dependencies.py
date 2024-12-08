from fastapi import FastAPI

from sqlalchemy import Engine
from typing import Any

from .database import make_postgres_connection
app = FastAPI()


async def common(q: Engine | None = None):
    return {"dbh": make_postgres_connection()}
