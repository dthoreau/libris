from sqlalchemy import create_engine, Engine
from typing import Any, Type, TypeVar
from pydantic import BaseModel

from sqlalchemy import Select, Insert, Table

import logging
logger = logging.getLogger()

ModelType = TypeVar('ModelType', bound=BaseModel)


def make_postgres_connection() -> Engine:
    engine = create_engine(
        "postgresql+psycopg2://libris@localhost/libris",
        echo=True)

    return engine


def get_all(common: dict[str, Any],
            query: Select,
            model_type: Type[ModelType]) -> list[ModelType]:
    collection = []
    eng: Engine = common["eng"]
    with eng.connect() as dbh:
        logger.warning(f'{query=}')
        query = query.limit(common["limit"]).offset(common["skip"])
        for row in dbh.execute(query):
            temp = model_type.model_validate(row._asdict())
            collection.append(temp)

        return collection


def get_one(common: dict[str, Any],
            query: Select,
            model_type: Type[ModelType]) -> ModelType:
    eng: Engine = common["eng"]
    with eng.connect() as dbh:
        for row in dbh.execute(query):
            return model_type.model_validate(row._asdict())

def insert(common: dict[str, Any],
           table: Table, new_record: BaseModel) -> None:
    stmt = Insert(table).values(new_record.model_dump())
    eng: Engine = common["eng"]
    with eng.connect() as dbh:
        dbh.execute(stmt)  
        dbh.commit()      
