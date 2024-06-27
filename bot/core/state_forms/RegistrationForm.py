from aiogram.fsm.state import State, StatesGroup


class RegistrationForm(StatesGroup):
    telegram_id = State()
    name = State()
    email = State()