from typing import Any, List, Optional, Union, Dict

from starlette_admin import BaseModelView
from starlette_admin import StringField
from starlette.requests import Request

from sqlalchemy import Table
from app import database
from . import deps

import logging


class ExtendModelView(BaseModelView):
    pk_attr = "id"
    ds: database.DataBase
    table: Table

    search_builder = False

    def __init__(self, ds, identity, *,
                 name, label, icon,
                 want_fields, table):
        self.ds = ds
        super().__init__()
        self.identity = identity
        self.name = name
        self.label = label
        self.icon = icon
        self.sortable_fields = want_fields
        self.fields = [StringField(field) for field in want_fields]

        self.ds = ds
        self.table = Table

    async def count(
            self, request: Request,
            where: Union[Dict[str, Any], str, None] = None) -> int:
        if self.identity == 'author':
            return database.count_authors(self.ds, where=where)

    async def find_all(
            self, request: Request,
            skip: int = 0,
            limit: int = 100,
            where: Union[Dict[str, Any], str, None] = None,
            order_by: Optional[List[str]] = None,) -> list[Any]:

        qslice = deps.QuerySlice(skip, limit)
        logging.info('>')
        qfields = [
            identity_to_field(self.ds, self.identity, field)
            for field in self.sortable_fields]

        try:
            retv = self.ds.reader().get_fields(
                fields=qfields, where=where,
                order=order_by, qslice=qslice)
            return retv
        except Exception as e:
            logging.info(e)
            raise e

    async def find_by_pk(self, _, pk):
        logging.info(f'{self.identity}')
        if self.identity == 'author':
            return database.get_author_by_id(self.ds, pk)
        if self.identity == 'book':
            return database.get_book_by_id(self.ds, pk)

    async def create(self, request: Request, data: Dict) -> object:
        pass

    async def edit(self, request: Request, pk, data: Dict):
        pass

    async def delete(self, request: Request,
                     pks: List[Any]) -> Optional[int]:
        pass


def identity_to_field(ds: database.DataBase, identity, field):
    meta = ds.metadata
    table = meta[f'{identity}s']

    for column in table.columns:
        if column.name == field:
            return column
