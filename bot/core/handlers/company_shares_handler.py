from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.core.logger.logger import drop_owner_logger as logger
from bot.core.common.ErrorMessage import send_error_message

from bot.core.services.CompanySharesService import CompanyShareService
from bot.core.keyboards.company_shares.shares_keyboard import SharesKeyboard

router = Router()


@router.callback_query(F.data.contains('/company_shares'))
async def main_menu(callback: CallbackQuery):
    try:
        text = 'Выберите акции:'
        keyboard = SharesKeyboard().get_buttons()

        await callback.message.answer(text=text, reply_markup=keyboard)
    except:
        await send_error_message('/company_shares', callback.message, logger)


@router.callback_query(F.data.contains('/get_share_'))
async def get_share(callback: CallbackQuery):
    share = callback.data.split('_')[-1]

    info = CompanyShareService.get_share_info(share)

    await callback.message.answer(text=info)
