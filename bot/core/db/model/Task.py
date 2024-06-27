from peewee import *
from bot.core.db.model.BaseModel import BaseModel


class Task(BaseModel):
    id = PrimaryKeyField(null=False)
    user_id = CharField(null=False)
    type = IntegerField(null=False)
    value = IntegerField(null=False)
