import logging

trader_logger = logging.getLogger("tg.bot.handler.trader")
admin_logger = logging.getLogger("tg.bot.handler.admin")
main_logger = logging.getLogger("tg.bot.handler.main")
drop_owner_logger = logging.getLogger("tg.bot.handler.drop_owner")


def create(level: int):
    logging.basicConfig(filename='../logs/logs.log',
                        filemode='w',
                        format='[%(asctime)s:%(levelname)s] [%(name)s] %(message)s',
                        level=level)

    logging.info('Bot started!')
