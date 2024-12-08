import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from app import schemas, services, dependencies


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/books", tags=["Books"]) 
def get_all_books(common: Annotated[dict, Depends(dependencies.common)]) -> list[schemas.Author]:
    return services.all_books(common)
