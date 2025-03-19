import logging

from app import database, schemas
from app.util import deps, passwords

log = logging.getLogger('api')


def get_all_users(ds, qslice: deps.Slice) -> list[schemas.User]:
    return database.get_all_users(ds, qslice)


def get_user_by_id(ds, id) -> schemas.User:
    return database.get_user_by_id(ds, id)


def delete_user(ds, id) -> None:
    database.delete_user(ds, id)


def enable_user(ds, id) -> None:
    database.enable_user(ds, id)


def create_user(ds, user: schemas.UserCreate) -> schemas.User:
    temp = {'username': user.username,
            'email': user.email,
            'full_name': user.full_name,
            'disabled': False,
            'hashed_password': passwords.get_password_hash(user.password)}
    return database.create_user(ds, temp)


def update_user(ds, id, user) -> schemas.User:
    return database.update_user(ds, id, user)
