from loader import bot
import json
from config_data import config
from config_data.load_settings import load
from telebot.types import Message

@bot.message_handler(commands=["settings"])
def set_settings(message: Message):
    if str(message.chat.id) != config.ADMIN_ID:
        return
    setup = json.load(settings)
    mess = message.text.split()
    if len(mess) < 3:
            bot.send_message(message.chat.id, "Параметр не найден \n /settings <setting> <value>")
            bot.send_message(message.chat.id, "Существующие параметры:\n" + "\n".join(setup.keys()))
            return
    setting = message.text.split()[1]
    value = " ".join(message.text.split()[2:])
    with open("settings.json", "r") as settings:
        if setting not in setup.keys():
            bot.send_message(message.chat.id, "Параметр не найден \n /settings <setting> <value>")
            bot.send_message(message.chat.id, "Существующие параметры:\n" + "\n".join(setup.keys()))
            return
        setup[setting] = value
    with open("settings.json", "w") as settings:
        json.dump(setup, settings)
    load()
