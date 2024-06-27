from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.core.services.MetalsService import MetalsService

class MetalsKeyboard:

    @classmethod
    def get_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        data = MetalsService.get_keyboard_data()

        for metal in data.keys():
            key.button(text=data[metal], callback_data=f'/get_metal_{metal}')
            key.adjust(1)

        return key.as_markup()
