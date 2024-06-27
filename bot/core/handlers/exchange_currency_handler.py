from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.core.logger.logger import drop_owner_logger as logger
from bot.core.common.ErrorMessage import send_error_message

from bot.core.services.UserService import UserService
from bot.core.keyboards.exchange_currency.exchange_keyboard import ExchangeCurrencyButton

router = Router()


@router.callback_query(F.data.contains('/currency_exchange'))
async def main_menu(callback: CallbackQuery):
    try:
        user_id = callback.from_user.id

        text = 'Выберите действие:'
        keyboard = ExchangeCurrencyButton().get_register_user_buttons()

        if not UserService.is_user_registered(user_id):
            text = 'Вы не зарегистрированы в приложении!'
            keyboard = ExchangeCurrencyButton().get_unregister_user_buttons()

        await callback.message.answer(text=text, reply_markup=keyboard)
    except:
        await send_error_message('/currency_exchange', callback.message, logger)


@router.callback_query(F.data.contains('/create_transaction'))
async def create_transaction(callback: CallbackQuery):
    pass
