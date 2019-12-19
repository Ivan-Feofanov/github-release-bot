import json
from typing import ByteString
from unittest.mock import patch

from aiogram.types import ParseMode
from starlette import status
from starlette.responses import Response

import settings
from utils import create_signature


@patch('bot.bot.send_message')
def test_custom_message(mock, client, custom_body):
    parse_mode = None
    if custom_body.get('parse_mode') == 'markdown':
        parse_mode = ParseMode.MARKDOWN
    elif custom_body.get('parse_mode') == 'html':
        parse_mode = ParseMode.HTML

    body: ByteString = json.dumps(custom_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)

    response: Response = client.post(
        '/message/', json=custom_body, headers={'X-Hub-Signature': sign})

    assert response.status_code == status.HTTP_200_OK
    mock.assert_called_once_with(
        chat_id=custom_body['chat_id'],
        text=custom_body['text'],
        parse_mode=parse_mode)
