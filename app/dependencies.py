from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy import Connection

# from .database import make_postgres_connection
app = FastAPI()


async def common_parameters(conn: Connection):
    return {"conn": conn}

CommonsDep = Annotated[dict, Depends(common_parameters)]
