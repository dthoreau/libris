from fastapi import Depends, FastAPI

from .dependencies import get_query_token

from .routers import books

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
