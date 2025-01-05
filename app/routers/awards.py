import logging

from fastapi import APIRouter

from app import schemas, services
from app.util import deps


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/awards", tags=["Awards"])
def get_all_awards(ds: deps.DataSource, qslice: deps.Slice
                   ) -> list[schemas.Award]:
    return services.all_awards(ds, qslice)


@router.get("/awards/{award}", tags=["Awards"])
def get_award(ds: deps.DataSource, qslice: deps.Slice,
              award: str) -> schemas.AwardExtended:
    return services.get_award(ds, award, qslice)


@router.get("/awards/{award}/books", tags=["Awards"])
def get_award_books(ds: deps.DataSource, qslice: deps.Slice,
                    award: str) -> list[schemas.Book]:
    return services.get_award_books(ds, award, qslice)


@router.delete("/awards/{award_id}", tags=["Awards"])
def delete_award():
    return NotImplementedError


@router.post("/awards", tags=["Awards"])
def create_award(ds: deps.DataSource,
                 award: schemas.AwardCreate) -> schemas.Award:
    return services.add_award(ds, award)


@router.put("/awards/{award_id}", tags=["Awards"])
def update_award():
    return NotImplementedError
