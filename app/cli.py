import uvicorn


def main() -> None:
    uvicorn.Server(uvicorn.Config(  # type: ignore[misc]
        "app.routers:app", port=8000, reload=True)).run()


main()
