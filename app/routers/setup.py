import logging
from fastapi import FastAPI

from . import books

libris_version = '0.0.1'

logger = logging.getLogger(__name__)

logger.info(f'Bookting Libris v{libris_version}')


app = FastAPI(
    title="Meis Libris",
    version=libris_version,
    openapi_tags=[]
)

for router in [books.router]:
    app.include_router(router)
