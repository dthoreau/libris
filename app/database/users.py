from sqlalchemy import Select

from app import schemas
from app.database import tables, DataBase
from app.util import deps


def get_all_users(ds: DataBase, qslice: deps.Slice) -> list[schemas.User]:
    stmt = Select(tables.users.c.id,
                  tables.users.c.username,
                  tables.users.c.email,
                  tables.users.c.full_name,
                  tables.users.c.hashed_password,
                  tables.users.c.disabled)
    return ds.reader().get_all(stmt, schemas.User, qslice)


def get_user_by_id(ds: DataBase, id: str) -> schemas.User:
    stmt = Select(
        tables.users.c.id,
        tables.users.c.username,
        tables.users.c.email,
        tables.users.c.full_name,
        tables.users.c.hashed_password,
        tables.users.c.disabled,
    ).where(tables.users.c.id == id)
    return ds.reader().get_one(stmt, schemas.User)


def delete_user(ds: DataBase, id: str) -> None:
    with ds.writer() as dw:
        temp = {'disabled': True}
        dw.update(tables.users, id, temp)


def enable_user(ds: DataBase, id: str) -> None:
    with ds.writer() as dw:
        temp = {'disabled': False}
        dw.update(tables.users, id, temp)


def create_user(ds: DataBase, user: schemas.UserCreate) -> None:
    with ds.writer() as dw:
        dw.insert(tables.users, user)


def update_user(ds: DataBase, id: str,
                user: schemas.UserCreate) -> schemas.User:
    pass
    # return database.update_user(ds, id: str, user)
