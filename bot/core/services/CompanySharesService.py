import requests


class CompanyShareService:
    BUTTON_ALL_CURRENCIES = 'ALL'
    INFO_MASK = ('#SHARE_NAME#(#SHARE#): \nЦена на открытии торгов: #VALUE_1# ₽'
                 '\nНаименьшая стоимость: #VALUE_2# ₽'
                 '\nНаивысшая стоимость: #VALUE_3# ₽'
                 '\nЦена перед закрытием торгов: #VALUE_4# ₽')

    @classmethod
    def get_share_info(cls, share):
        data = cls.get_share_data([share], share == cls.BUTTON_ALL_CURRENCIES)
        return cls.__prepare_share_info(data)

    @classmethod
    def get_share_data(cls, shares, is_all):
        share_data = []

        if is_all:
            shares = cls.__get_data()

        for share in shares:
            request = requests.get(
                f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{share}/.json').json()

            print(request)
            share_data.append([
                share,
                request['marketdata']['data'][0][9], request['marketdata']['data'][0][10],
                request['marketdata']['data'][0][11], request['marketdata']['data'][0][12]
            ])

        return share_data

    @classmethod
    def __prepare_share_info(cls, array):
        data = cls.__get_data()
        info = 'Данные по запросу: \n'
        for item in array:
            info += (cls.INFO_MASK.replace('#SHARE_NAME#', data[item[0]]).
                     replace('#SHARE#', item[0]).
                     replace('#VALUE_1#', str(item[1])).
                     replace('#VALUE_2#', str(item[2])).
                     replace('#VALUE_3#', str(item[3])).
                     replace('#VALUE_4#', str(item[4])) + '\n')

        return info

    @classmethod
    def __get_data(cls) -> dict:
        return {
            'GAZP': 'Газпром',
            'TATN': 'Татнефть',
            'AFLT': 'Аэрофлот',
            'SBER': 'Сбербанк',
            'CHMF': 'Северсталь',
            'VKCO': 'Вконтакте',
            'ROSN': 'Роснефть',
            'PLZL': 'Полюс',
            'GMKN': 'Норильский никель',
        }

    @classmethod
    def get_keyboard_data(cls) -> dict:
        keyboard = cls.__get_data()
        keyboard[cls.BUTTON_ALL_CURRENCIES] = 'Все акции'
        return keyboard
