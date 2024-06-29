from peewee import *
from bot.core.db.model.BaseModel import BaseModel
from bot.core.db.model.Users import Users


class Task(BaseModel):
    id = PrimaryKeyField(null=False)
    user_id = ForeignKeyField(Users, to_field='telegram_id')
    type = IntegerField(null=False)
    value = IntegerField(null=False)
