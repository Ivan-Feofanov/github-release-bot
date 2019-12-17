from fastapi import APIRouter
from starlette import status
from starlette.background import BackgroundTasks
from starlette.responses import Response

from bot import proceed_release, proceed_deploy
from models import Body, Actions, Deploy

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


@api_router.post('/deploy/')
async def deploy(*,
                 body: Deploy,
                 chat_id: str = None,
                 background_tasks: BackgroundTasks):

    background_tasks.add_task(proceed_deploy, body, chat_id)
    return Response(status_code=status.HTTP_200_OK)
