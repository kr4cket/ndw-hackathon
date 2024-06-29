from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.core.services.NotifierService import NotifierService
from bot.core.services.CurrencyService import CurrencyService
from bot.core.services.CompanySharesService import CompanyShareService
from bot.core.services.MetalsService import MetalsService

class NotifyKeyboard:

    @classmethod
    def get_notify_type_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        data = NotifierService.get_notify_services_buttons()

        for notify in data.keys():
            key.button(text=data[notify]['name'], callback_data=f'/notify_type_{notify}')

        key.button(text='Вернуться на главную', callback_data='/start')
        key.adjust(1)
        return key.as_markup()

    @classmethod
    def get_notify_value_buttons(cls, type) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        service_class = NotifierService.get_notify_service_class(type)
        data = eval(f'{service_class}.get_keyboard_data()')

        for notify in data.keys():
            key.button(text=data[notify], callback_data=f'/notify_value_{notify}')

        key.button(text='Вернуться на главную', callback_data='/start')
        key.adjust(1)
        return key.as_markup()
