import asyncio
import time

from bot.core.db.model.Notifier import Notifier
from bot.core.db.model.Task import Task
from bot.core.common.TelegramBot import TelegramBot
from datetime import datetime, timedelta
from bot.core.services.CurrencyService import CurrencyService
from bot.core.services.CompanySharesService import CompanyShareService
from bot.core.services.MetalsService import MetalsService


class NotifierService:
    __services = {
        'company_shares': {
            'class': 'CompanyShareService',
            'method': 'get_share_info',
        },
        'currency': {
            'class': 'CurrencyService',
            'method': 'get_currency_info',
        },
        'metals': {
            'class': 'MetalsService',
            'method': 'get_metal_info',
        },
    }

    @classmethod
    def __get_service(cls, type):
        return cls.__services[type]

    @classmethod
    def create_notify(cls, data):
        Notifier.create(**data)

    @classmethod
    def create_task(cls, data):
        task = Task.create(**data)

        notify_data = {
            'task_id': task.id,
            'time': datetime.now() + timedelta(hours=task.time_interval),
        }

        cls.create_notify(notify_data)

    @classmethod
    def update_notify_time(cls, time_interval):
        Notifier.update(time=datetime.now() + timedelta(hours=time_interval)).execute()

    @classmethod
    def execute_task(cls, task_id):
        task = Task.get(Task.id == task_id)
        service = cls.__get_service(task.type)
        text = cls.execute_task_action(service['class'], service['method'], task.value)
        cls.update_notify_time(task.time_interval)
        asyncio.run(cls.notify(text, task.user_id.telegram_id))


    @classmethod
    def execute_task_action(cls, service, method, value):
        return eval(f"{service}.{method}('{value}')")

    @classmethod
    async def notify(cls, text, user):
        bot = TelegramBot()
        await bot.send_message(chat_id=int(user), text=text)

    @classmethod
    def check_available_task(cls):
        notifies = Notifier.select().where(Notifier.time < datetime.now())
        for notify in notifies:
            cls.execute_task(notify.task_id)

    @classmethod
    def start_service(cls):
        while True:
            cls.check_available_task()
            time.sleep(60)
