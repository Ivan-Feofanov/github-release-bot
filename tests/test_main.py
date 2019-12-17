from unittest.mock import patch

import pytest
from starlette import status
from starlette.responses import Response

from utils import prepare_markdown


@pytest.mark.parametrize('url', ('/release/', '/deploy/'))
@patch('bot.bot.send_message')
def test_main_unauthorized(mock, client, release_body, url):
    response: Response = client.post(url, json=release_body)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    mock.assert_not_called()


def test_prepare_markdown():
    incoming_body = '### title\n\r* abc\r\n'
    result = prepare_markdown(incoming_body)
    assert result == 'title\n\r- abc\r\n'
