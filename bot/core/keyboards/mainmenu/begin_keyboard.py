from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BeginKeyboard:
    @classmethod
    def get_main_menu_button(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Главное меню', callback_data='/start')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_cancel_registration_button(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Отменить регистрацию', callback_data='/cancel_registration')
        key.adjust(1)

        return key.as_markup()
