from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Menu:
    @classmethod
    def get_unregister_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Акции', callback_data='/company_shares')
        key.button(text='Металлы', callback_data='/metals')
        key.button(text='Валюта', callback_data='/currency')
        key.button(text='Обмен валюты', callback_data='/currency_exchange')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_register_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Акции', callback_data='/company_shares')
        key.button(text='Металлы', callback_data='/metals')
        key.button(text='Валюта', callback_data='/currency')
        key.button(text='Обмен валюты', callback_data='/currency_exchange')
        key.button(text='Создать напоминание', callback_data='/create_notify')
        key.adjust(1)

        return key.as_markup()
