import hashlib
import hmac
from typing import ByteString

from fastapi import HTTPException
from starlette import status

import settings
from models import Body


def create_signature(key: ByteString, message: ByteString) -> str:
    return 'sha1=' + hmac.new(key, message, hashlib.sha1).hexdigest()


def check_auth(body: ByteString, outer_sign: str):
    inner_sign = create_signature(settings.SECRET_TOKEN.encode(), body)

    if not hmac.compare_digest(outer_sign, inner_sign):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def prepare_markdown(text: str) -> str:
    return text\
        .replace('*', '-')\
        .replace('### ', '')


def make_message(body: Body) -> str:
    release = body.release
    verb = body.action.capitalize()
    return f'Project: *{body.repository.name}*\n\r' \
           f'{verb} release *{release.name} ({release.tag_name})*.' \
           f'\n\r\n\r' \
           f'*Release notes:* \n\r\n\r{prepare_markdown(release.body)}\n\r'
