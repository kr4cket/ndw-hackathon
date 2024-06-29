from aiogram.fsm.state import State, StatesGroup


class CreateTaskForm(StatesGroup):
    user_id = State()
    type = State()
    value = State()
    time_interval = State()
