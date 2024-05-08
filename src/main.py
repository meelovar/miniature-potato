import click
from aiohttp import web

from routes import (
    hash,
    healthcheck,
)

@click.command
@click.option("--host", default="0.0.0.0", help="Bind to this host")
@click.option("--port", default=8080, help="Bind to this port")
def main(host: str, port: int) -> None:
    app = create_app()

    web.run_app(app, host=host, port=port)


def create_app() -> web.Application:
    app = web.Application()

    return setup_app(app)


def setup_app(app: web.Application) -> web.Application:
    routes = (
        web.get("/healthcheck", healthcheck),
        web.post("/hash", hash),
    )

    app.add_routes(routes)

    return app


if __name__ == "__main__":
    main()
