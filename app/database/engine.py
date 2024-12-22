from sqlalchemy import create_engine, Engine


def make_postgres_connection() -> Engine:
    engine = create_engine(
        "postgresql+psycopg2://libris@localhost/libris",
        echo=True)

    return engine
