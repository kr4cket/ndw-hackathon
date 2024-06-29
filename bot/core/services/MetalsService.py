import requests
import datetime
import xmltodict

from bot.core.services.AgregationService import AgregationService
from bot.core.db.model.Metals import Metal

class MetalsService:
    BUTTON_ALL_CURRENCIES = 'ALL'
    INFO_MASK = 'Курс #METAL#: #VALUE# ₽'

    @classmethod
    def get_metal_info(cls, metal):
        data = cls.get_metal_data(metal)
        return cls.__prepare_metal_info(data)

    @classmethod
    def get_metal_data(cls, metal_request_id):
        metals = []
        metal_data = Metal.select().dicts().get_or_none()
        if metal_data is None:
            metal_data = AgregationService.get_metals()


        if metal_request_id == cls.BUTTON_ALL_CURRENCIES:
            for metal in metal_data:
                metals.append([metal['code'], metal['value']])
        else:
            for metal in metals:
                if int(metal['code']) == int(metal_request_id):
                    metals.append([metal['code'], metal['value']])
                    break

        return metals

    @classmethod
    def __prepare_metal_info(cls, array):
        info = 'Данные по запросу: \n'
        data = cls.__get_data()
        for item in array:
            info += (cls.INFO_MASK.replace('#METAL#', data[str(item[0])]).
                     replace('#VALUE#', str(item[1])) + '\n')

        return info

    @classmethod
    def __get_data(cls) -> dict:
        return {
            '1': 'Золото',
            '2': 'Серебро',
            '3': 'Платина',
            '4': 'Палладий',
        }

    @classmethod
    def get_keyboard_data(cls) -> dict:
        keyboard = cls.__get_data()
        keyboard[cls.BUTTON_ALL_CURRENCIES] = 'Все металлы'
        return keyboard
