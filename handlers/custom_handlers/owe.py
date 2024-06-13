msg = """Вы не оплатили участие в турнире. Через некоторое время вы будете удалены из турнира. 
Если вы не хотите участвовать в соревновании, введите команду /delete. По всем вопросам обращайтесь в тг @PavelNihg или вк https://vk.com/pavel_aleks2015"""

from loader import bot, base
from telebot.types import Message
from config_data import config


@bot.message_handler(commands=["owe"])
def reminder(message: Message):
    bot.send_message(config.ADMIN_ID, "owe start")
    players = base.debtor()
    for elem in players:
        bot.send_message(elem[0], msg)
        bot.send_message(config.ADMIN_ID, base.get_nickname_player(elem[0]) + " не оплатил")
    bot.send_message(config.ADMIN_ID, "owe finish")


@bot.message_handler(commands=["owe_player"])
def reminder(message: Message):
    bot.send_message(config.ADMIN_ID, "owe start")
    if str(message.chat.id) != config.ADMIN_ID:
        return
    if len(message.text.split()) != 2:
        bot.send_message(config.ADMIN_ID, "Некорректная команда \n /owe_player <id>")
    user_id = message.text.split()[1]
    bot.send_message(user_id, msg)
    bot.send_message(config.ADMIN_ID, base.get_nickname_player(user_id) + " не оплатил")
    bot.send_message(config.ADMIN_ID, "owe finish")