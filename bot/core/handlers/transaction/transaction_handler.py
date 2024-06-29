from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.core.state_forms.TransactionForm import CreateTransactionForm
from bot.core.keyboards.mainmenu.begin_keyboard import BeginKeyboard
from bot.core.keyboards.exchange_currency.exchange_keyboard import ExchangeCurrencyButton
from bot.core.services.UserService import UserService
from bot.core.services.TransactionService import TransactionService

router = Router()


@router.callback_query(F.data.contains('/create_transaction'))
async def start_registration(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Для выбора получателя транзакции, введите его почту или никнейм',
                                  reply_markup=BeginKeyboard().get_main_menu_button())
    await state.set_state(CreateTransactionForm.receiver)


@router.message(CreateTransactionForm.receiver)
async def first_step_registration(message: types.Message, state: FSMContext):
    receiver_id = UserService.get_user(message.text)
    if receiver_id < 0:
        await message.answer(text=f'Пользователя, которого вы ищите, нет в системе!',
                             reply_markup=ExchangeCurrencyButton().get_retry_operation_buttons())
        return

    await message.answer(text='Введите суммую, которую хотите перечислить:',
                         reply_markup=BeginKeyboard().get_main_menu_button())
    await state.update_data(receiver=receiver_id)
    await state.update_data(sender=message.from_user.id)
    await state.set_state(CreateTransactionForm.value)


@router.message(CreateTransactionForm.value)
async def last_step_registration(message: types.Message, state: FSMContext):
    await state.update_data(value=message.text)
    TransactionService.create_transaction(await state.get_data())
    await message.answer(text=f'Отлично, транзакция создана!',
                         reply_markup=ExchangeCurrencyButton().get_final_operation_buttons())


@router.callback_query(F.data.contains('/get_active_transaction_by_me'))
async def get_active_transaction_by_me(callback: CallbackQuery):
    data = TransactionService.get_active_sender_transactions(callback.from_user.id)
    text = f"Транзакция №{data['id']}\n{data['user_type']}: {data['user']}\nСумма: {data['value']}"

    await callback.message.answer(text=text,
                                  reply_markup=ExchangeCurrencyButton().get_active_transaction_tool(data['id'],
                                                                                                    data['prev_id'],
                                                                                                    data['next_id'],
                                                                                                    data['by_user']))


@router.callback_query(F.data.contains('/get_active_transaction_by_users'))
async def get_active_transaction_by_users(callback: CallbackQuery):
    data = TransactionService.get_active_receiver_transactions(callback.from_user.id)
    text = f"Транзакция №{data['id']}\n{data['user_type']}: {data['user']}\nСумма: {data['value']}"

    await callback.message.answer(text=text,
                                  reply_markup=ExchangeCurrencyButton().get_active_transaction_tool(data['id'],
                                                                                                    data['prev_id'],
                                                                                                    data['next_id'],
                                                                                                    data['by_user']))


@router.callback_query(F.data.contains('/get_transaction_'))
async def get_active_transaction(callback: CallbackQuery):
    type = callback.data.split('_')[-1]
    id = int(callback.data.split('_')[-2])
    data = TransactionService.get_active_transaction(id, type)
    text = f"Транзакция №{data['id']}\n{data['user_type']}: {data['user']}\nСумма: {data['value']}"

    await callback.message.answer(text=text,
                                  reply_markup=ExchangeCurrencyButton().get_active_transaction_tool(data['id'],
                                                                                                    data['prev_id'],
                                                                                                    data['next_id'],
                                                                                                    data['by_user']))


@router.callback_query(F.data.contains('/accept_transaction_'))
async def get_active_transaction(callback: CallbackQuery):
    id = callback.data.split('_')[-1]
    TransactionService.accept_transaction(id)
    text = f"Транзакция одобрена!"

    await callback.message.answer(text=text,
                                  reply_markup=ExchangeCurrencyButton.get_active_transaction_tool_type())

@router.callback_query(F.data.contains('/decline_transaction_'))
async def get_active_transaction(callback: CallbackQuery):
    id = callback.data.split('_')[-1]
    TransactionService.decline_transaction(id)
    text = f"Транзакция отменена!"

    await callback.message.answer(text=text,
                                  reply_markup=ExchangeCurrencyButton.get_active_transaction_tool_type())