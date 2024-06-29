import datetime
from peewee import *
from bot.core.db.model.BaseModel import BaseModel
from bot.core.db.model.Users import Users

class Transaction(BaseModel):
    id = PrimaryKeyField(null=False)
    sender = ForeignKeyField(Users, to_field='telegram_id')
    receiver = ForeignKeyField(Users, to_field='telegram_id')
    value = IntegerField(null=False)
    type = IntegerField(default=1)
    time = DateTimeField(default=datetime.datetime.now)
