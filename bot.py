import os

import aiohttp
from aiogram import Bot
from aiogram.types import ParseMode, Message

from models import Body

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

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)


def prepare_markdown(text: str) -> str:
    return text\
        .replace('*', '-')\
        .replace('###', '*')\
        .replace('\n\r', '*\n\r')\
        .replace('\r\n', '*\r\n')


def make_message(body: Body) -> str:
    release = body.release
    verb = 'Drafted' if release.draft else 'Published'
    return f'Project: *{body.repository.name}*\n\r' \
           f'{verb} new release *{release.name} ({release.tag_name})*.\n\r' \
           f'Release notes: \n\r\n\r{prepare_markdown(release.body)}\n\r'


async def proceed_release(body: Body) -> Message:
    return await bot.send_message(
        chat_id=CHAT_ID,
        text=make_message(body),
        parse_mode=ParseMode.MARKDOWN)
