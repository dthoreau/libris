import logging
from fastapi import FastAPI

from . import books

from app.database import make_postgres_connection
from starlette_admin.contrib.sqla import Admin

from .admin import setup_admin


libris_version = '0.0.1'

logger = logging.getLogger(__name__)

logger.info(f'Bookting Libris v{libris_version}')


app = FastAPI(
    title="Meis Libris",
    version=libris_version,
    openapi_tags=[]
)
engine = make_postgres_connection()
admin = Admin(engine, 'Libris')

setup_admin(admin)

for router in [books.router]:
    app.include_router(router)

admin.mount_to(app)
