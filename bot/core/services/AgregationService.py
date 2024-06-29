import asyncio
import time
import xmltodict

import requests

from bot.core.db.model.Notifier import Notifier
from bot.core.db.model.Task import Task
from bot.core.common.TelegramBot import TelegramBot
from datetime import datetime, timedelta, date



class AgregationService:

    @classmethod
    def get_notify_services_buttons(cls):
        return cls.__services

    @classmethod
    def get_notify_service_class(cls, name):
        return cls.__services[name]['class']

    @classmethod
    def __get_service(cls, type):
        return cls.__services[type]

    @classmethod
    def create_notify(cls, data):
        Notifier.create(**data)

    @classmethod
    def get_metals(cls):
        dates = date.today().strftime('%d/%m/%Y')
        metals = requests.get(
            f'https://cbr.ru/scripts/xml_metall.asp?date_req1={dates}&date_req2={dates}').content
        metals = xmltodict.parse(metals)['Metall']
        data = []
        for metal in metals['Record']:
            data.append({'code': metal['@Code'], 'value': metal['Sell']})

        return data

    @classmethod
    def get_currency(cls):
        requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    @classmethod
    def get_share(cls, share):
        request = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{share}/.json').json()
        return {
            'code': share,
            'value': request['marketdata']['data'][0][9],
            'high': request['marketdata']['data'][0][10],
            'low': request['marketdata']['data'][0][11],
            'end': request['marketdata']['data'][0][12],
        }



    @classmethod
    def update_data(cls):
        pass

    @classmethod
    def start_service(cls):
        while True:
            cls.update_data()
            time.sleep(300)
