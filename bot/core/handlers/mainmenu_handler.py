from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.core.services.UserService import UserService
from bot.core.logger.logger import main_logger as logger
from bot.core.common.ErrorMessage import send_error_message


router = Router()


@router.callback_query(F.data.contains('/start'))
@router.message(CommandStart())
async def bot_start(callback, state: FSMContext):
    try:
        await state.clear()
        user_id = callback.from_user.id
        if type(callback) is CallbackQuery:
            callback = callback.message

        keyboard = UserService().get_keyboard(user_id)
        await callback.answer(text='Вы в главном меню', reply_markup=keyboard)
    except:
        await send_error_message('/start', callback, logger)
