import json
from typing import ByteString

import respx
from starlette import status
from starlette.responses import Response

import settings
from utils import create_signature


@respx.mock
def test_custom_message(client, custom_body, bot_url):
    body: ByteString = json.dumps(custom_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    request = respx.mock.post(bot_url, status_code=200)
    response: Response = client.post(
        '/message/', json=custom_body, headers={'X-Hub-Signature': sign})

    assert response.status_code == status.HTTP_200_OK
    assert request.called
