import configparser
from aiogram import Bot
from aiogram.enums import ParseMode


class TelegramBot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            parser = configparser.ConfigParser()
            parser.read('../settings.ini')
            api_key = parser['Bot']['tokenapi']
            token = api_key
            cls._instance = Bot(token, parse_mode=ParseMode.HTML)

        return cls._instance
