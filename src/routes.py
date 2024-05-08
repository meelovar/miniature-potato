from aiohttp import web

from services import hash_sha256_string
from validators import validate_field


async def healthcheck(_: web.Request) -> web.Response:
    return web.json_response({})


@validate_field("string")
async def hash(request: web.Request) -> web.Response:
    data = await request.json()
    result = hash_sha256_string(data["string"])

    return web.json_response({"hash_string": result})
