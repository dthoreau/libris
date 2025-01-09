import logging
from fastapi import FastAPI

from app.database import DataBase
from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.contrib.sqla import Admin

from traceback import print_exception

from sqlalchemy import create_engine

from .admin import setup_admin

from . import authors, awards, books, genres, series, subjects

libris_version = '0.0.1'

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

logger.info(f'Booting Libris v{libris_version}')

app = FastAPI(
    title="Meis Libris",
    version=libris_version,
    openapi_tags=[]
)


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print_exception(e)
        return Response('Internal Server Error', status_code=500)

app.middleware('http')(catch_exceptions_middleware)

ds = DataBase()
engine = create_engine(
            "postgresql+psycopg2://libris@localhost/libris",
            echo=True)

admin = Admin(ds.engine, 'Libris')

setup_admin(admin, ds)

for router in [authors.router,
               awards.router,
               books.router,
               genres.router,
               series.router,
               subjects.router]:
    app.include_router(router)

admin.mount_to(app)
