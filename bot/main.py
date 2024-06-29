import asyncio
import threading
from bot.core.logger import logger

from aiogram import Dispatcher

from bot.core.handlers import mainmenu_handler, currency_handler, company_shares_handler, metals_handler, exchange_currency_handler, notify_handler
from bot.core.handlers.registration import user_registration_handler
from bot.core.handlers.transaction import transaction_handler
from bot.core.common.TelegramBot import TelegramBot
from bot.core.services.NotifierService import NotifierService

bot = TelegramBot()
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
    dp.include_router(notify_handler.router)
    dp.include_router(currency_handler.router)

    threading.Thread(target=NotifierService().start_service).start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
