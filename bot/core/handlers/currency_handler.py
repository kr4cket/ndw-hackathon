from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.core.logger.logger import drop_owner_logger as logger
from bot.core.common.ErrorMessage import send_error_message

from bot.core.keyboards.currency.currency_keyboard import CurrencyKeyboard
from bot.core.services.CurrencyService import CurrencyService

router = Router()


@router.callback_query(F.data.contains('/currency'))
async def main_menu(callback: CallbackQuery):
    try:
        text = 'Выберите валюту:'
        keyboard = CurrencyKeyboard().get_buttons()

        await callback.message.answer(text=text, reply_markup=keyboard)
    except:
        await send_error_message('/currency', callback.message, logger)


@router.callback_query(F.data.contains('/get_currency_'))
async def get_currency(callback: CallbackQuery):
    currency = callback.data.split('_')[-1]
    info = CurrencyService.get_currency_info(currency)

    await callback.message.answer(text=info)
