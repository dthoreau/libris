from typing import NoReturn
import uvicorn


def main() -> NoReturn:
    config = uvicorn.Config("app.routers:app", port=8000, reload=True)

    uvicorn.Server(config).run()


main()
