import json
from typing import ByteString
from unittest.mock import patch

from starlette import status
from starlette.responses import Response

import settings
from utils import create_signature


@patch('bot.bot.send_message')
def test_deploy(mock, client, deploy_body):
    body: ByteString = json.dumps(deploy_body).encode()
    sign = create_signature(settings.SECRET_TOKEN.encode(), body)
    response: Response = client.post(
        '/deploy/', json=deploy_body, headers={'X-Hub-Signature': sign})
    assert response.status_code == status.HTTP_200_OK
    mock.assert_called_once()
