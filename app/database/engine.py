from sqlalchemy import create_engine, Engine, Connection, func
from typing import Type, TypeVar
from pydantic import BaseModel

from sqlalchemy import (Select, Insert, Delete, Update,
                        Table, desc, BinaryExpression)

from . import tables

import logging
import yaml

logger = logging.getLogger('engine')

ModelType = TypeVar('ModelType', bound=BaseModel)


class DataBase(object):
    engine: Engine
    dbh: Connection
    metadata: dict[str, Table]

    def __init__(self) -> None:

        with open('config.yaml') as config:
            try:
                config = yaml.safe_load(config)
                connection_string = config[0]['connection']

            except Exception as e:
                raise e

        logger.info('Connecting...')
        self.engine = create_engine(connection_string, echo=False, )

        self.metadata = tables.metadata()
        self.dbh = self.engine.connect()

    def get_engine(self) -> Engine:
        return self.engine

    def reader(self):
        return DataReader()

    def writer(self):
        return DataWriter()


class DataReader(DataBase):
    pass

    def get_fields(self, *, fields, where, order, qslice):
        stmt = Select(*fields)
        if where is not None:
            stmt = stmt.where(fields[1].ilike(f'%{where}%'))
        stmt = make_order(stmt, order, qslice)

        return self.dbh.execute(stmt)

    def get_all(self,
                query: Select,
                model_type: Type[ModelType],
                *, qslice: object | None = None,
                order: str | None = None) -> list[ModelType]:
        collection: list[ModelType] = []
        logger.info(f'DB> SELECT all {model_type}')

        query = make_order(query, order, qslice)

        for row in self.dbh.execute(query):
            temp = model_type.model_validate(row._asdict())
            collection.append(temp)
        return collection

    def get_one(self,
                query: Select,
                model_type: Type[ModelType]) -> ModelType:
        logger.info(f'DB> SELECT one {model_type} {query}')

        for row in self.dbh.execute(query):
            payload = model_type.model_validate(row._asdict())
            return payload

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
        self.dbh.begin()
        return self

    def insert(self, table: Table,
               new_record: BaseModel | dict[str, str]) -> any:
        logger.info(f'DB> Insert: {table=}')
        if type(new_record) is dict:
            stmt = Insert(table).values([new_record])
        else:
            stmt = Insert(table).values(
                new_record.model_dump(exclude_none=True))  # type: ignore[misc]

        try:
            crsr = self.dbh.execute(stmt)
        except Exception as e:
            self.dbh.rollback()
            logger.error(f'Error inserting into {table}: {e}')
            raise e
        return crsr.inserted_primary_key[0]  # type: ignore[return-value]

    def delete(self, table: Table, id: str) -> None:
        logger.info(f'DB> Delete from {table} {id=}')
        stmt = Delete(table).where(table.c.id == id)
        try:
            self.dbh.execute(stmt)
        except Exception as e:
            self.dbh.rollback()
            logger.error(f'Error deleting {table} {id}: {e}')
            raise e

    # TODO this doesn't actually work, using run_update_stmt instead
    def delete_pivot_entry(self, table: Table,
                           record: dict[str, str]) -> None:
        logger.info(f'DB> Delete from pivot {table} {record}')
        stmt = Delete(table).where([record])

        logger.info(stmt)
        try:
            self.dbh.execute(stmt)
        except Exception as e:
            self.dbh.rollback()
            logger.error(f'Error deleting pivot entry: {e}')
            raise e

    def run_update_stmt(self, stmt) -> int:
        result = self.dbh.execute(stmt)

        return result.rowcount

    def update(self, table: Table, id: str, update: object) -> None:
        logger.info(f'DB> UPDATE {table} {id=}')
        if type(update) is dict:
            stmt = Update(table).where(table.c.id == id).values(update)
        else:
            stmt = Update(table).where(table.c.id == id).values(
                update.model_dump())

        try:
            self.dbh.execute(stmt)
        except Exception as e:
            self.dbh.rollback()
            logger.error(f'Error updating {table} {id}: {e}')
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info('DB> Autocommit')
        self.dbh.commit()


def make_order(stmt: Select, orderlist, qslice):
    if orderlist is not None:
        field, otype = orderlist[0].split()
        if otype == 'desc':
            stmt = stmt.order_by(desc(field))
        else:
            stmt = stmt.order_by(field)

    if qslice is not None:
        stmt = stmt.limit(qslice.limit).offset(qslice.skip)

    return stmt
