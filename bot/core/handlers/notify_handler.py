import re
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.core.logger.logger import drop_owner_logger as logger
from bot.core.common.ErrorMessage import send_error_message

from bot.core.keyboards.notify.notify_keyboard import NotifyKeyboard
from bot.core.keyboards.mainmenu.begin_keyboard import BeginKeyboard
from bot.core.services.NotifierService import NotifierService
from bot.core.state_forms.TaskForm import CreateTaskForm

router = Router()


@router.callback_query(F.data.contains('/create_notify'))
async def main_menu(callback: CallbackQuery, state: FSMContext):
    try:
        text = 'Выберите тип нотификации:'
        keyboard = NotifyKeyboard().get_notify_type_buttons()

        await state.set_state(CreateTaskForm.type)
        await state.update_data(user_id=callback.from_user.id)
        await callback.message.answer(text=text, reply_markup=keyboard)
    except:
        await send_error_message('/create_notify', callback.message, logger)


@router.message(CreateTaskForm.type)
@router.callback_query(F.data.contains('/notify_type_'))
async def set_type(callback: CallbackQuery, state: FSMContext):
    type = callback.data.split('_')[-1]

    text = 'Выберите котировку:'
    keyboard = NotifyKeyboard().get_notify_value_buttons(type)

    await state.set_state(CreateTaskForm.value)
    await state.update_data(type=type)
    await callback.message.answer(text=text, reply_markup=keyboard)


@router.message(CreateTaskForm.value)
@router.callback_query(F.data.contains('/notify_value_'))
async def set_value(callback: CallbackQuery, state: FSMContext):
    value = callback.data.split('_')[-1]
    text = 'Введите интервал нотификации (мин.):'

    await state.set_state(CreateTaskForm.time_interval)
    await state.update_data(value=value)
    await callback.message.answer(text=text)


@router.message(CreateTaskForm.time_interval)
async def set_time(message: types.Message, state: FSMContext):
    value = message.text

    if not re.match('^\\d+$', value):
        value = 15

    text = 'Нотификация успешно создана!'

    await state.update_data(time_interval=value)

    data = await state.get_data()
    NotifierService.create_task(data)

    await message.answer(text=text, reply_markup=BeginKeyboard.get_main_menu_button())
