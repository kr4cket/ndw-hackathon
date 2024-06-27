from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.core.services.CurrencyService import  CurrencyService

class CurrencyKeyboard:

    @classmethod
    def get_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        data = CurrencyService.get_keyboard_data()

        for share in data.keys():
            key.button(text=data[share], callback_data=f'/get_currency_{share}')
            key.adjust(1)

        return key.as_markup()
