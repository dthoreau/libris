import logging

from fastapi import APIRouter

from app import schemas, services


from app.util import deps

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/series", tags=["Series"])
def get_all_series(ds: deps.DataSource, slice: deps.Slice) -> \
        list[schemas.Series]:
    return services.all_series(ds, slice)


@router.get("/series/{series}", tags=["Series"])
def get_series(ds: deps.DataSource,  series_id: str) -> schemas.Series:
    return services.get_series(ds, series_id)


@router.get("/series/{series}/books", tags=["Series"])
def get_series_books(ds: deps.DataSource, slice: deps.Slice,
                     series: str) -> list[schemas.Book]:
    return services.get_series_books(ds, slice, series)


@router.get("/series/{series_id}", tags=["Series"])
def get_series_by_id():
    return NotImplementedError


@router.delete("/series/{series_id}", tags=["Series"])
def delete_series():
    return NotImplementedError


@router.post("/series", tags=["Series"])
def create_series():
    return NotImplementedError


@router.put("/series/{series_id}", tags=["Series"])
def update_series():
    return NotImplementedError
