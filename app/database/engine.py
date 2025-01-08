from sqlalchemy import create_engine, Engine, Connection
from typing import Type, TypeVar
from pydantic import BaseModel

from sqlalchemy import Select, Insert, Table, Delete, Update

import logging
logger = logging.getLogger()

ModelType = TypeVar('ModelType', bound=BaseModel)


class DataBase(object):
    engine: Engine
    dbh: Connection

    def __init__(self) -> None:
        self.engine = create_engine(
            "postgresql+psycopg2://libris@localhost/libris",
            echo=True)

        self.dbh = self.engine.connect()

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
                slice: object) -> list[ModelType]:
        collection: list[ModelType] = []

        query = query.limit(slice.limit).offset(slice.skip)
        for row in self.dbh.execute(query):
            temp = model_type.model_validate(row._asdict())
            collection.append(temp)

        return collection

    def get_one(self,
                query: Select,
                model_type: Type[ModelType]) -> ModelType:

        try:
            for row in self.dbh.execute(query):
                payload = model_type.model_validate(row._asdict())
                return payload
        except Exception as e:
            raise e


class DataWriter(DataBase):
    pass

    def __enter__(self):
        return self

    def insert(self, table: Table, new_record: BaseModel) -> None:
        stmt = Insert(table).values(
            new_record.model_dump())  # type: ignore[misc]

        self.dbh.execute(stmt)

    def delete(self, table: Table, id: str) -> None:
        stmt = Delete(table).where(table.c.id == id)

        self.dbh.execute(stmt)

    def update(self, table: Table, id: str, update: object) -> None:
        stmt = Update(table).where(table.c.id == id).values(
            update.model_dump())

        try:
            self.dbh.execute(stmt)
        except Exception as e:
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbh.commit()
