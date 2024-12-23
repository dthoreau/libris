import logging
from app.database import make_postgres_connection

logger = logging.getLogger(__name__)


async def common(
        skip: int = 0, limit: int = 100):
    eng = make_postgres_connection()
    return {"skip": skip, "limit": limit, "eng": eng}
