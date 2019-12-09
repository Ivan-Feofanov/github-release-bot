import json
from typing import ByteString
from unittest.mock import patch

from starlette import status
from starlette.responses import Response

import settings
from utils import create_signature, prepare_markdown


@patch('bot.bot.send_message')
def test_main(mock, client, message_body):
    body: ByteString = json.dumps(message_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        '/release/', json=message_body, headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK
    mock.assert_called_once()


@patch('bot.bot.send_message')
def test_main_unauthorized(mock, client, message_body):
    response: Response = client.post('/release/', json=message_body)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    mock.assert_not_called()


def test_prepare_markdown():
    incoming_body = '### title\n\r* abc\r\n'
    result = prepare_markdown(incoming_body)
    assert result == '*title*\n\r- abc*\r\n'
