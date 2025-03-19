import logging

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def check_password(hashed: str, password: str) -> bool:

    matches = pwd_context.verify(password, hashed)
    logging.info(f'password {matches=}')

    return matches
