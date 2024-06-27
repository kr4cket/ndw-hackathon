from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ExchangeCurrencyButton:
    @classmethod
    def get_unregister_user_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Главное меню', callback_data='/start')
        key.button(text='Регистрация', callback_data='/register')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_register_user_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Создать транзакцию', callback_data='/create_transaction')
        key.button(text='Активные транзакции', callback_data='/get_active_transactions')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_active_transaction_tool(cls, id, is_last=False) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Принять транзакцию', callback_data='/accept_transaction')
        key.button(text='Отменить транзакцию', callback_data='/decline_transaction')

        if not is_last:
            key.button(text='Следущая транзакция', callback_data=f'/next_transaction_{id}')
        key.adjust(1)

        return key.as_markup()
