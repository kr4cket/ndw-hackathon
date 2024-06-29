from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ExchangeCurrencyButton:
    @classmethod
    def get_unregister_user_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Главное меню', callback_data='/start')
        key.button(text='Регистрация', callback_data='/register')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_register_user_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Создать транзакцию', callback_data='/create_transaction')
        key.button(text='Активные транзакции', callback_data='/get_active_transactions_menu')
        key.button(text='Главное меню', callback_data='/start')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_active_transaction_tool(cls, id,prev_id=None, next_id=None, by_users=False) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        transaction_type = 'me'

        if by_users:
            transaction_type = 'users'
            key.button(text='Принять транзакцию', callback_data=f'/accept_transaction_{id}')
        key.button(text='Отменить транзакцию', callback_data=f'/decline_transaction_{id}')

        if prev_id:
            key.button(text='Предыдущая транзакция', callback_data=f'/get_transaction_{prev_id}_{transaction_type}')

        if next_id:
            key.button(text='Следующая транзакция', callback_data=f'/get_transaction_{next_id}_{transaction_type}')

        key.button(text='Вернуться в главное меню', callback_data='/start')

        key.adjust(1)
        return key.as_markup()

    @classmethod
    def get_retry_operation_buttons(cls):
        key = InlineKeyboardBuilder()

        key.button(text='Повторить создание транзакции', callback_data='/create_transaction')
        key.button(text='Вернуться в главное меню', callback_data='/start')
        key.adjust(1)
        return key.as_markup()

    @classmethod
    def get_final_operation_buttons(cls):
        key = InlineKeyboardBuilder()

        key.button(text='Повторить создание транзакции', callback_data='/create_transaction')
        key.button(text='Посмотреть активные транзакции', callback_data='/get_active_transactions_menu')
        key.button(text='Вернуться в главное меню', callback_data='/start')
        key.adjust(1)
        return key.as_markup()

    @classmethod
    def get_active_transaction_tool_type(cls):
        key = InlineKeyboardBuilder()

        key.button(text='Созданные транзакции', callback_data='/get_active_transaction_by_me')
        key.button(text='Полученные транзакции', callback_data='/get_active_transaction_by_users')
        key.button(text='Вернуться в главное меню', callback_data='/start')
        key.adjust(1)
        return key.as_markup()


    @classmethod
    def get_active_transactions(cls):
        key = InlineKeyboardBuilder()

        key.button(text='Посмотреть', callback_data='/currency_exchange')
        key.adjust(1)
        return key.as_markup()
