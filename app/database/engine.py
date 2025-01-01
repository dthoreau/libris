from sqlalchemy import create_engine, Engine
from typing import Type, TypeVar
from pydantic import BaseModel

from sqlalchemy import Select, Insert, Table

import logging
logger = logging.getLogger()

ModelType = TypeVar('ModelType', bound=BaseModel)


class DataBase(object):
    engine: Engine

    def __init__(self) -> None:
        self.engine = create_engine(
            "postgresql+psycopg2://libris@localhost/libris",
            echo=True)

    def get_engine(self) -> Engine:
        return self.engine

    def reader(self):
        return DataReader()

    def writer(self):
        return DataWriter()


class DataReader(DataBase):
    pass

    def get_all(self,
                query: Select,
                model_type: Type[ModelType],
                slice: dict[str, int]) -> list[ModelType]:
        collection: list[ModelType] = []

        with self.engine.connect() as dbh:

            query = query.limit(slice["limit"]).offset(slice["skip"])
            for row in dbh.execute(query):
                temp = model_type.model_validate(row._asdict())
                collection.append(temp)

        return collection

    def get_one(self,
                query: Select,
                model_type: Type[ModelType]) -> ModelType:

        with self.engine.connect() as dbh:
            for row in dbh.execute(query):
                return model_type.model_validate(row._asdict())


class DataWriter(DataBase):
    pass

    def insert(self, table: Table, new_record: BaseModel) -> None:
        stmt = Insert(table).values(
            new_record.model_dump())  # type: ignore[misc]
        engine: Engine = self.engine
        with engine.connect() as dbh:
            dbh.execute(stmt)
            dbh.commit()

    def __del__(self):
        with self.engine.connect() as dbh:
            dbh.commit()
