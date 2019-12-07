import os

from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

from bot import proceed_release
from models import Body

ONLY_PUBLISH = os.getenv('ONLY_PUBLISH', False)

app = FastAPI()


@app.post("/")
async def read_root(body: Body):
    if not (body.release.draft and ONLY_PUBLISH):
        await proceed_release(body)
    return Response(status_code=status.HTTP_200_OK)
