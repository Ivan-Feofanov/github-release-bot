from fastapi import FastAPI, HTTPException, Depends
from starlette import status
from starlette.requests import Request

import settings
from router import api_router
from utils import check_auth

docs_kwargs = {}
if settings.ENVIRONMENT == 'production':
    docs_kwargs = dict(docs_url=None, redoc_url=None)  # noqa: pylint=invalid-name

app = FastAPI(**docs_kwargs)


async def check_auth_middleware(request: Request):
    if settings.ENVIRONMENT in ('production', 'test'):
        body = await request.body()
        if not check_auth(body, request.headers.get('X-Hub-Signature', '')):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


app.include_router(api_router, dependencies=[Depends(check_auth_middleware)])
