from aiogram.fsm.state import State, StatesGroup


class CreateTransactionForm(StatesGroup):
    sender = State()
    receiver = State()
    type = State()
    value = State()
