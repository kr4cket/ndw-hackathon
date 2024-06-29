import datetime

from bot.core.keyboards.mainmenu.unregister_user_menu import Menu
from bot.core.db.model.Transaction import Transaction


class TransactionService:

    @classmethod
    def get_active_transaction(cls, transaction_id: int, type: str):
        transaction = (Transaction
                       .select()
                       .where(Transaction.id == transaction_id)
                       .get_or_none())
        if not transaction:
            return None

        transaction_type = Transaction.receiver
        user_id = transaction.receiver
        by_user = False
        user = transaction.sender.email
        user_type = 'Отправитель'

        if type == 'me':
            transaction_type = Transaction.sender
            user_id = transaction.sender
            by_user = True
            user = transaction.receiver.email
            user_type = 'Получатель'

        next = cls.get_next_element_id(transaction_type, user_id, transaction.time)
        prev = cls.get_prev_element_id(transaction_type, user_id, transaction.time)

        return {
            'value': transaction.value,
            'id': transaction.id,
            'prev_id': prev,
            'next_id': next,
            'user_type': user_type,
            'user': user,
            'by_user': by_user,
        }

    @classmethod
    def get_active_receiver_transactions(cls, user_id: int):
        transaction = (Transaction
                       .select()
                       .where(Transaction.receiver.telegram_id == user_id and Transaction.type == 1)
                       .order_by(Transaction.time.desc())
                       .limit(1)
                       .get_or_none())
        if not transaction:
            return None

        next = cls.get_next_element_id(Transaction.receiver, user_id, transaction.time)
        prev = cls.get_prev_element_id(Transaction.receiver, user_id, transaction.time)

        return {
            'value': transaction.value,
            'id': transaction.id,
            'prev_id': prev,
            'next_id': next,
            'user_type': 'Отправитель',
            'user': transaction.sender,
            'by_user': True,
        }

    @classmethod
    def get_active_sender_transactions(cls, user_id: int):
        transaction = (Transaction
                       .select()
                       .where(Transaction.sender.telegram_id == user_id and Transaction.type == 1)
                       .order_by(Transaction.time.desc())
                       .limit(1)
                       .get_or_none())

        if not transaction:
            return None

        next = cls.get_next_element_id(Transaction.sender, user_id, transaction.time)
        prev = cls.get_prev_element_id(Transaction.sender, user_id, transaction.time)

        return {
            'value': transaction.value,
            'id': transaction.id,
            'prev_id': prev,
            'next_id': next,
            'user_type': 'Получатель',
            'user': transaction.receiver,
            'by_user': False,
        }

    @classmethod
    def create_transaction(cls, data: dict):
        Transaction.create(**data)

    @classmethod
    def get_next_element_id(cls, obj: object, user_id: int, time: datetime.datetime):
        transaction = (Transaction
                       .select()
                       .where(obj.telegram_id == user_id and Transaction.type == 1 and Transaction.time < time)
                       .order_by(Transaction.time.desc())
                       .limit(1)
                       .get_or_none())
        if not transaction:
            return None

        return transaction.id

    @classmethod
    def get_prev_element_id(cls, obj: object, user_id: int, time: datetime.datetime):
        transaction = (Transaction
                       .select()
                       .where(obj.telegram_id == user_id and Transaction.type == 1 and Transaction.time > time)
                       .order_by(Transaction.time.asc())
                       .limit(1)
                       .get_or_none())
        if not transaction:
            return None

        return transaction.id

    @classmethod
    def accept_transaction(cls, id: int):
        print(id)

        Transaction.update(type=2).where(Transaction.id == id).execute()

    @classmethod
    def decline_transaction(cls, id: int):
        print(id)
        Transaction.update(type=0).where(Transaction.id == id).execute()
