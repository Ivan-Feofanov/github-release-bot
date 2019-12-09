import os

import aiohttp
from aiogram import Bot
from aiogram.types import ParseMode, Message

from models import Body
from utils import make_message

TOKEN = os.getenv('TOKEN', '110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw')
CHAT_ID = os.getenv('CHAT_ID', 'CHAT_ID')

# Proxy settings
PROXY_URL = os.getenv('PROXY_URL')
PROXY_USERNAME = os.getenv('PROXY_USERNAME')
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')
PROXY_AUTH = None

if PROXY_URL and PROXY_USERNAME and PROXY_PASSWORD:
    PROXY_AUTH = aiohttp.BasicAuth(
        login=PROXY_USERNAME, password=PROXY_PASSWORD)

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)  # noqa: pylint=invalid-name


async def proceed_release(body: Body, chat_id: str) -> Message:
    return await bot.send_message(
        chat_id=chat_id,
        text=make_message(body),
        parse_mode=ParseMode.MARKDOWN)
