import requests
import datetime
import xmltodict


class MetalsService:
    BUTTON_ALL_CURRENCIES = 'ALL'
    INFO_MASK = 'Курс #METAL#: #VALUE# ₽'

    @classmethod
    def get_metal_info(cls, metal):
        data = cls.get_metal_data(metal)
        return cls.__prepare_metal_info(data)

    @classmethod
    def get_metal_data(cls, metal_request_id):
        metal_data = []
        date = datetime.date.today().strftime('%d/%m/%Y')
        metals = requests.get(
            f'https://cbr.ru/scripts/xml_metall.asp?date_req1={date}&date_req2={date}').content
        metals = xmltodict.parse(metals)['Metall']

        if metal_request_id == cls.BUTTON_ALL_CURRENCIES:
            for metal in metals['Record']:
                metal_data.append([metal['@Code'], metal['Sell']])
        else:
            for metal in metals['Record']:
                if int(metal['@Code']) == int(metal_request_id):
                    metal_data.append([metal['@Code'], metal['Sell']])
                    break

        return metal_data

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
