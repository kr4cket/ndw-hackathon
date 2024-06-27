# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Task(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    user_id = CharField(max_length=255)
    type = IntegerField()
    value = IntegerField()
    class Meta:
        table_name = "task"


@snapshot.append
class Notifier(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    task_id = snapshot.ForeignKeyField(index=True, model='task')
    time = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "notifier"


@snapshot.append
class User(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    telegram_id = IntegerField()
    class Meta:
        table_name = "user"


@snapshot.append
class Transaction(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    sender = snapshot.ForeignKeyField(index=True, model='user')
    receiver = snapshot.ForeignKeyField(index=True, model='user')
    type = IntegerField()
    time = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "transaction"


def forward(old_orm, new_orm):
    user = new_orm['user']
    return [
        # Apply default value 0 to the field user.telegram_id,
        user.update({user.telegram_id: 0}).where(user.telegram_id.is_null(True)),
    ]
