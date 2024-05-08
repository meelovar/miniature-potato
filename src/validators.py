import json
from typing import (
    Awaitable,
    Callable,
)

from aiohttp import web

type RouteType = Callable[[web.Request], Awaitable[web.Response]]


def validate_field(field_name: str) -> Callable[[RouteType], RouteType]:
    def decorator(fn: RouteType) -> RouteType:
        async def wrapper(request: web.Request) -> web.Response:
            data = await request.json()

            if field_name not in data:
                error_body = json.dumps({"validation_errors": f"Missing required field: '{field_name}'"})

                raise web.HTTPBadRequest(text=error_body, content_type="application/json")

            return await fn(request)

        return wrapper

    return decorator
