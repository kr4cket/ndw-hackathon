import asyncio
import configparser
from aiogram.enums import ParseMode
from bot.core.logger import logger

from aiogram import Bot, Dispatcher

from bot.core.handlers import mainmenu_handler, currency_handler, company_shares_handler, metals_handler, exchange_currency_handler
from bot.core.handlers.registration import user_registration_handler
from bot.core.handlers.transaction import transaction_handler

parser = configparser.ConfigParser()
parser.read('../settings.ini')
api_key = parser['Bot']['tokenapi']

TOKEN_API = api_key
bot = Bot(TOKEN_API, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Уровень логов
PRODUCTION = 30  # При запуске на Прод
DEBUG = 10  # При разработке

async def main() -> None:
    logger.create(DEBUG)

    dp.include_router(mainmenu_handler.router)
    dp.include_router(exchange_currency_handler.router)
    dp.include_router(user_registration_handler.router)
    dp.include_router(transaction_handler.router)
    dp.include_router(metals_handler.router)
    dp.include_router(company_shares_handler.router)
    dp.include_router(currency_handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
