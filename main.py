from fastapi import FastAPI, Header
from starlette import status
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import Response

from bot import proceed_release
from models import Body, Actions
from utils import check_auth

app = FastAPI()  # noqa: pylint=invalid-name


@app.post("/release/")
async def release(*,
                  body: Body,
                  chat_id: str = None,
                  release_only: bool = False,
                  request: Request,
                  x_hub_signature: str = Header(''),
                  background_tasks: BackgroundTasks):

    check_auth(await request.body(), x_hub_signature)

    if (body.release.draft and not release_only) \
            or body.action == Actions.released:
        background_tasks.add_task(proceed_release, body, chat_id)

    return Response(status_code=status.HTTP_200_OK)
