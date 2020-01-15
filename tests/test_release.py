import json
from typing import ByteString
from unittest.mock import patch

import pytest
import respx
from starlette import status
from starlette.responses import Response

import settings
from models import Actions
from utils import create_signature


@respx.mock
def test_main(client, release_body, bot_url):
    body: ByteString = json.dumps(release_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    request = respx.mock.post(bot_url, status_code=200)
    response: Response = client.post(
        '/release/', json=release_body, headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK
    assert request.called


@respx.mock
@pytest.mark.parametrize('action', (x for x in Actions))
@pytest.mark.parametrize('draft', (True, False))
@pytest.mark.parametrize('release_only', (True, False))
def test_filter_by_action(
        client, release_body, action, draft, release_only, bot_url):
    release_body['action'] = action
    release_body['release']['draft'] = draft

    request = respx.mock.post(bot_url, status_code=200)
    body: ByteString = json.dumps(release_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        f'/release/?release_only={release_only}',
        json=release_body,
        headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK

    if action == Actions.released or (draft and not release_only):
        assert request.called
    else:
        assert not request.called
