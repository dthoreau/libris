import logging
from fastapi import APIRouter
from app import schemas, services
from app.util import deps

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/users", tags=['Users'])
def get_all_users(ds: deps.DataSource,
                  qslice: deps.Slice) -> list[schemas.User]:
    return services.get_all_users(ds, qslice)


@router.get("/user/{user_id}", tags=['Users'])
def get_user(ds: deps.DataSource, id: str) -> schemas.User:
    return services.get_user_by_id(ds, id)


@router.delete("/users/{user_id}", tags=['Users'])
def delete_user(ds: deps.DataSource, id: str) -> None:
    services.delete_user(ds, id)
    pass


@router.put("/users/{user_id}/enable", tags=['Users'])
def enable_user(ds: deps.DataSource, id: str) -> None:
    services.enable_user(ds, id)


@router.post("/users", tags=['Users'])
def create_user(ds: deps.DataSource,
                user: schemas.UserCreate) -> None:
    services.create_user(ds, user)


@router.put("/users/{user_id}", tags=['Users'])
def update_user(ds: deps.DataSource, id: str,
                user: schemas.UserCreate) -> schemas.User:
    return services.update_user(ds, id, user)
