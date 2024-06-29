from peewee import *
from bot.core.db.model.BaseModel import BaseModel
from bot.core.db.model.Users import Users


class Task(BaseModel):
    id = PrimaryKeyField(null=False)
    user_id = ForeignKeyField(Users, to_field='telegram_id')
    type = CharField(null=False)
    value = CharField(null=False)
    time_interval = IntegerField(null=False)
