from unittest.mock import patch

import pytest
import respx
from starlette import status
from starlette.responses import Response

from utils import prepare_markdown


@respx.mock
@pytest.mark.parametrize('url', ('/release/', '/message/'))
def test_main_unauthorized(client, release_body, url):
    request = respx.mock.post(url, status_code=200)
    response: Response = client.post(url, json=release_body)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert not request.called


def test_prepare_markdown():
    incoming_body = '### title\n\r* abc\r\n'
    result = prepare_markdown(incoming_body)
    assert result == 'title\n\r- abc\r\n'
