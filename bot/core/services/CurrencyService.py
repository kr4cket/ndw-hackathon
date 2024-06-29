import requests
from bot.core.services.AgregationService import AgregationService

class CurrencyService:
    BUTTON_ALL_CURRENCIES = 'ALL'
    INFO_MASK = 'Курс #CURRENCY#: #VALUE# ₽'

    @classmethod
    def get_currency_info(cls, currency):
        data = cls.get_currency_data([currency], currency == cls.BUTTON_ALL_CURRENCIES)
        return cls.__prepare_currency_info(data)

    @classmethod
    def get_currency_data(cls, currency, is_all):
        request = cls.__get_request_data()
        currency_data = []

        if is_all:
            currency = cls.__get_data().keys()

        for item in currency:
            currency_data.append([item, request['Valute'][item]['Value'], request['Valute'][item]['Nominal']])

        return currency_data

    @classmethod
    def __prepare_currency_info(cls, array):
        info = 'Данные по запросу: \n'
        for item in array:
            info += (cls.INFO_MASK.replace('#CURRENCY#', str(item[0])).
                     replace('#VALUE#', str(item[1] / item[2])) + '\n')

        return info

    @classmethod
    def __get_data(cls) -> dict:
        return {
            'EUR': 'EUR',
            'USD': 'USD',
            'CNY': 'CNY',
            'KZT': 'KZT',
            'TRY': 'TRY',
            'JPY': 'JPY',
        }

    @classmethod
    def __get_request_data(cls):
        return AgregationService.get_currencies()

    @classmethod
    def get_keyboard_data(cls) -> dict:
        keyboard = cls.__get_data()
        keyboard[cls.BUTTON_ALL_CURRENCIES] = 'Все валюты'
        return keyboard

    @classmethod
    def get_currency_value(cls, currency) -> float:
        data = cls.__get_request_data()

        if currency in data['Valute']:
            return float(data['Valute'][currency]['Value'])

        return 0.0
