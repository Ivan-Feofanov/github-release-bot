import json
from typing import ByteString
from unittest.mock import patch

import pytest
from starlette import status
from starlette.responses import Response

import settings
from models import Actions
from utils import create_signature, prepare_markdown


@patch('bot.bot.send_message')
def test_main(mock, client, message_body):
    body: ByteString = json.dumps(message_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        '/release/', json=message_body, headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK


@patch('bot.bot.send_message')
def test_main_unauthorized(mock, client, message_body):
    response: Response = client.post('/release/', json=message_body)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    mock.assert_not_called()


def test_prepare_markdown():
    incoming_body = '### title\n\r* abc\r\n'
    result = prepare_markdown(incoming_body)
    assert result == 'title\n\r- abc\r\n'


@pytest.mark.parametrize('action', (x for x in Actions))
@pytest.mark.parametrize('draft', (True, False))
@pytest.mark.parametrize('release_only', (True, False))
@patch('bot.bot.send_message')
def test_filter_by_action(
        mock, client, message_body, action, draft, release_only):
    message_body['action'] = action
    message_body['release']['draft'] = draft

    body: ByteString = json.dumps(message_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        f'/release/?release_only={release_only}',
        json=message_body,
        headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK

    if action == Actions.released or (draft and not release_only):
        mock.assert_called_once()
    else:
        mock.assert_not_called()
