msg = """Вы не оплатили участие в турнире. Через некоторое время вы будете удалены из турнира. 
Если вы не хотите учатсвовать в соревновании, введите команду /delete. По всем вопросам обращайтесь в тг @PavelNihg или вк https://vk.com/pavel_aleks2015"""

from loader import bot, base
from telebot.types import Message
from config_data import config


@bot.message_handler(commands=["owe"])
def reminder(message: Message):
    bot.send_message(config.ADMIN_ID, "owe start")
    players = base.debtor()
    for elem in players:
        # bot.send_message(elem[0], msg)
        bot.send_message(config.ADMIN_ID, base.get_nickname_player(elem[0]) + " не оплатил")
    bot.send_message(config.ADMIN_ID, "owe finish")