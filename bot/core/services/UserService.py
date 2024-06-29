from bot.core.keyboards.mainmenu.unregister_user_menu import Menu
from bot.core.db.model.Users import Users as User


class UserService:

    @classmethod
    def get_keyboard(cls, user_id: int):
        if cls.is_user_registered(user_id):
            return Menu().get_register_buttons()

        return Menu().get_unregister_buttons()

    @classmethod
    def is_user_registered(cls, user_id: int):
        user = User.select().where(User.telegram_id == user_id).get_or_none()
        return True if user else False

    @classmethod
    def register_user(cls, data: dict):
        User.create(**data)

    @classmethod
    def get_user(cls, field):

        user = User.select().where(User.email == field).get_or_none()
        return user.telegram_id if user else -1
