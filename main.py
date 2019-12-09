from fastapi import FastAPI, Header
from starlette import status
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import Response

import settings
from bot import proceed_release
from models import Body
from utils import check_auth

app = FastAPI()  # noqa: pylint=invalid-name


@app.post("/release/")
async def release(*,
                  body: Body,
                  chat_id: str = None,
                  request: Request,
                  x_hub_signature: str = Header(''),
                  background_tasks: BackgroundTasks):

    check_auth(await request.body(), x_hub_signature)

    if not (body.release.draft and settings.ONLY_PUBLISH):
        background_tasks.add_task(proceed_release, body, chat_id)

    return Response(status_code=status.HTTP_200_OK)
