import json
from typing import ByteString
from unittest.mock import patch

import pytest
from starlette import status
from starlette.responses import Response

import settings
from models import Actions
from utils import create_signature


@patch('bot.bot.send_message')
def test_main(mock, client, release_body):
    body: ByteString = json.dumps(release_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        '/release/', json=release_body, headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize('action', (x for x in Actions))
@pytest.mark.parametrize('draft', (True, False))
@pytest.mark.parametrize('release_only', (True, False))
@patch('bot.bot.send_message')
def test_filter_by_action(
        mock, client, release_body, action, draft, release_only):
    release_body['action'] = action
    release_body['release']['draft'] = draft

    body: ByteString = json.dumps(release_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        f'/release/?release_only={release_only}',
        json=release_body,
        headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK

    if action == Actions.released or (draft and not release_only):
        mock.assert_called_once()
    else:
        mock.assert_not_called()
