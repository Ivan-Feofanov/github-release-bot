from fastapi import APIRouter
from starlette import status
from starlette.background import BackgroundTasks
from starlette.responses import Response

from bot import proceed_release, proceed_custom
from models import Body, Actions, Message

api_router = APIRouter()  # noqa: pylint=invalid-name


@api_router.post("/release/")
async def release(*,
                  body: Body,
                  chat_id: str = None,
                  release_only: bool = False,
                  background_tasks: BackgroundTasks):

    if (body.release.draft and not release_only) \
            or body.action == Actions.released:
        background_tasks.add_task(proceed_release, body, chat_id)

    return Response(status_code=status.HTTP_200_OK)


@api_router.post('/message/')
async def message(body: Message, background_tasks: BackgroundTasks):
    background_tasks.add_task(proceed_custom, body)
    return Response(status_code=status.HTTP_200_OK)
