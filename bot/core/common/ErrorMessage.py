from aiogram import types

from bot.core.keyboards.mainmenu.begin_keyboard import BeginKeyboard


async def send_error_message(command: str, callback: types.Message, logger):
    logger.exception(f"Ошибка во время выполнения команды '{command}'", )

    await callback.answer(text="Ошибка во время выполнения команды!\nПовторите попытку позднее",
                          reply_markup=BeginKeyboard().get_main_menu_button())
