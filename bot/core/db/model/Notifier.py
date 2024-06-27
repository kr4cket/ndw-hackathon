import datetime

from peewee import *
from bot.core.db.model.BaseModel import BaseModel
from bot.core.db.model.Task import Task


class Notifier(BaseModel):
    id = PrimaryKeyField(null=False)
    task_id = ForeignKeyField(Task, to_field='id')
    time = DateTimeField(default=datetime.datetime.now)
