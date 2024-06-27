from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.core.services.CompanySharesService import CompanyShareService


class SharesKeyboard:

    @classmethod
    def get_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        data = CompanyShareService.get_keyboard_data()

        for share in data.keys():
            key.button(text=data[share], callback_data=f'/get_share_{share}')
            key.adjust(1)

        return key.as_markup()
