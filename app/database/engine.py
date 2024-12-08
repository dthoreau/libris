from sqlalchemy import create_engine, Connection


def make_postgres_connection() -> Connection:
    engine = create_engine(
        "postgresql+psycopg2://libris@localhost/libris",
        echo=True)

    with engine.connect() as conn:
        return conn
