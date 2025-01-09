from sqlalchemy import create_engine, Engine, Connection, func
from typing import Type, TypeVar
from pydantic import BaseModel

from sqlalchemy import (Select, Insert, Delete, Update,
                        Table, desc, BinaryExpression)

import logging
logger = logging.getLogger(__name__)

ModelType = TypeVar('ModelType', bound=BaseModel)


class DataBase(object):
    engine: Engine
    dbh: Connection

    def __init__(self) -> None:
        logger.info('Connecting...')
        self.engine = create_engine(
            "postgresql+psycopg2://libris@localhost/libris",
            echo=False)

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
                slice: object, *,
                order: str | None = None) -> list[ModelType]:
        collection: list[ModelType] = []
        logger.info(f'DB> SELECT all {model_type}')

        if order is not None:
            field, otype = order[0].split()
            if otype == 'desc':
                query = query.order_by(desc(field))
            else:
                query = query.order_by(field)

        query = query.limit(slice.limit).offset(slice.skip)
        for row in self.dbh.execute(query):
            temp = model_type.model_validate(row._asdict())
            collection.append(temp)
        return collection

    def get_one(self,
                query: Select,
                model_type: Type[ModelType]) -> ModelType:
        logger.info(f'DB> SELECT one {model_type}')

        try:
            for row in self.dbh.execute(query):
                payload = model_type.model_validate(row._asdict())
                return payload
        except Exception as e:
            raise e

    def count(self, table: Table, *,
              where: list[BinaryExpression] | None = None) -> int:
        stmt = Select(func.count()).select_from(table)
        if where is not None:
            stmt = stmt.where(*where)

        count = self.dbh.execute(stmt).scalar()
        logger.info(f'Rows {count=}')
        return count


class DataWriter(DataBase):
    pass

    def __enter__(self):
        return self

    def insert(self, table: Table, new_record: BaseModel) -> None:
        logger.info(f'DB> Insert: {table=}')
        stmt = Insert(table).values(
            new_record.model_dump())  # type: ignore[misc]

        self.dbh.execute(stmt)

    def delete(self, table: Table, id: str) -> None:
        logger.info(f'DB> Delete from {table} {id=}')
        stmt = Delete(table).where(table.c.id == id)

        self.dbh.execute(stmt)

    def update(self, table: Table, id: str, update: object) -> None:
        logger.info(f'DB> UPDATE {table} {id=}')
        stmt = Update(table).where(table.c.id == id).values(
            update.model_dump())

        try:
            self.dbh.execute(stmt)
        except Exception as e:
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info('DB> Autocommit')
        self.dbh.commit()
