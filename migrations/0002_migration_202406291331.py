# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Users(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    telegram_id = IntegerField(unique=True)
    class Meta:
        table_name = "users"


@snapshot.append
class Task(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    user_id = snapshot.ForeignKeyField(field='telegram_id', index=True, model='users')
    type = IntegerField()
    value = CharField(max_length=255)
    time_interval = IntegerField()
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
class Transaction(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    sender = snapshot.ForeignKeyField(field='telegram_id', index=True, model='users')
    receiver = snapshot.ForeignKeyField(field='telegram_id', index=True, model='users')
    value = IntegerField()
    type = IntegerField(default=1)
    time = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "transaction"


def forward(old_orm, new_orm):
    task = new_orm['task']
    old_task = old_orm['task']
    return [
        # Apply default value 0 to the field task.time_interval,
        task.update({task.time_interval: 0}).where(task.time_interval.is_null(True)),
        # Convert datatype of the field task.value: INT -> VARCHAR(255),
        task.update({task.value: old_task.value.cast('VARCHAR')}).where(old_task.value.is_null(False)),
    ]


def backward(old_orm, new_orm):
    old_task = old_orm['task']
    task = new_orm['task']
    return [
        # Convert datatype of the field task.value: VARCHAR -> INT,
        task.update({task.value: old_task.value.cast('INTEGER')}).where(old_task.value.is_null(False)),
    ]
