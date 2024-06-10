from loader import bot, base
from telebot.types import Message
from config_data import config


@bot.message_handler(commands=["reminder"])
def reminder(message: Message):
    players = base.reminder(base.get_now_tour())
    for elem in players:
        bot.send_message(elem[0], "Матчи скоро начнутся. Не забудьте сделать прогноз")
        bot.send_message(config.ADMIN_ID, base.get_nickname_player(elem[0]) + " не сделал прогноз")
        bot.send_message(config.ADMIN_ID2, base.get_nickname_player(elem[0]) + " не сделал прогноз")