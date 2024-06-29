import datetime

from peewee import *

from bot.core.db.model.BaseModel import BaseModel


class Stock(BaseModel):
    id = PrimaryKeyField(null=False)
    code = CharField(null=False, unique=True)
    value = DecimalField(null=False)
    high = DecimalField(null=False)
    low = DecimalField(null=False)
    end = DecimalField(null=False)
    time = DateTimeField(default=datetime.datetime.now())
