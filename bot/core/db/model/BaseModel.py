from peewee import *
from bot.core.db.db_conn import DBConnection


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        database = DBConnection().get_handle()
