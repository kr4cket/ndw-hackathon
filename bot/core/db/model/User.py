from peewee import *
from bot.core.db.model.BaseModel import BaseModel


class User(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    email = CharField(null=False)
    telegram_id = IntegerField(null=False)
