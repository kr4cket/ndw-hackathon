import datetime
from peewee import *
from bot.core.db.model.BaseModel import BaseModel
from bot.core.db.model.User import User

class Transaction(BaseModel):
    id = PrimaryKeyField(null=False)
    sender = ForeignKeyField(User, to_field='id')
    receiver = ForeignKeyField(User, to_field='id')
    type = IntegerField(null=False)
    time = DateTimeField(default=datetime.datetime.now)
