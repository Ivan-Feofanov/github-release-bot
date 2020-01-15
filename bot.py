import os
from urllib.parse import urljoin, quote

import httpx
from httpx import Response

from models import Body, Message
from settings import TG_API_URL
from utils import make_message


def get_url():
    proxy_url = os.getenv('PROXY_URL')
    base_url = proxy_url if proxy_url else TG_API_URL
    return urljoin(base_url, quote(f"bot{os.getenv('BOT_TOKEN')}/sendMessage"))


async def proceed_release(body: Body, chat_id: str) -> Response:
    data = dict(
        chat_id=chat_id,
        text=make_message(body),
        parse_mode='markdown')
    url = get_url()
    async with httpx.AsyncClient() as client:
        return await client.post(url=url, json=data)


async def proceed_custom(message: Message) -> Response:
    data = dict(
        chat_id=message.chat_id,
        text=message.text)
    url = get_url()
    if message.parse_mode:
        data['parse_mode'] = message.parse_mode
    async with httpx.AsyncClient() as client:
        return await client.post(url=url, json=data)
