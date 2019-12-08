from unittest.mock import patch

from starlette import status
from starlette.responses import Response

from bot import prepare_markdown


@patch('bot.bot.send_message')
def test_main(mock, client, message_body):
    response: Response = client.post('/', json=message_body)
    assert response.status_code == status.HTTP_200_OK
    mock.assert_called_once()


def test_prepare_markdown():
    incoming_body = '###title\n\r* abc\r\n'
    result = prepare_markdown(incoming_body)
    assert result == '*title*\n\r- abc*\r\n'
