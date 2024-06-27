from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.core.logger.logger import drop_owner_logger as logger
from bot.core.common.ErrorMessage import send_error_message

from bot.core.keyboards.metals.metals_keyboard import MetalsKeyboard
from bot.core.services.MetalsService import MetalsService

router = Router()


@router.callback_query(F.data.contains('/metals'))
async def main_menu(callback: CallbackQuery):
    try:
        text = 'Выберите металл:'
        keyboard = MetalsKeyboard().get_buttons()

        await callback.message.answer(text=text, reply_markup=keyboard)
    except:
        await send_error_message('/metals', callback.message, logger)


@router.callback_query(F.data.contains('/get_metal_'))
async def get_currency(callback: CallbackQuery):
    metal = callback.data.split('_')[-1]
    info = MetalsService.get_metal_info(metal)

    await callback.message.answer(text=info)
