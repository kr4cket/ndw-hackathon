from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.core.state_forms.RegistrationForm import RegistrationForm
from bot.core.keyboards.mainmenu.begin_keyboard import BeginKeyboard
from bot.core.services.UserService import UserService

router = Router()


@router.callback_query(F.data.contains('/register'))
async def start_registration(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Как вас зовут?', reply_markup=BeginKeyboard().get_cancel_registration_button())
    await state.set_state(RegistrationForm.name)


@router.message(RegistrationForm.name)
async def first_step_registration(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=f'Очень приятно, {message.text}, напиши свою электронную почту =)',
                         reply_markup=BeginKeyboard().get_cancel_registration_button())
    await state.set_state(RegistrationForm.email)


@router.message(RegistrationForm.email)
async def last_step_registration(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text, telegram_id=message.from_user.id)
    UserService.register_user(await state.get_data())

    await message.answer(text=f'Отлично, регистрация завершена!', reply_markup=BeginKeyboard().get_main_menu_button())
