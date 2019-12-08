from unittest.mock import patch

from starlette import status
from starlette.responses import Response


@patch('bot.bot.send_message')
def test_main(mock, client, message_body):
    response: Response = client.post('/', json=message_body)
    assert response.status_code == status.HTTP_200_OK
    mock.assert_called_once()
