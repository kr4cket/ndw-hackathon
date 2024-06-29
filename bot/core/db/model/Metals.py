import datetime

from peewee import *

from bot.core.db.model.BaseModel import BaseModel


class Metal(BaseModel):
    id = PrimaryKeyField(null=False)
    code = CharField(null=False, unique=True)
    value = DecimalField(null=False)
    time = DateTimeField(default=datetime.datetime.now())
