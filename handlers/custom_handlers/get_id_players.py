from loader import bot, base
from keyboards.reply import my_marcup
from config_data import config
from telebot.types import Message


@bot.message_handler(commands=["get_players"])
def get_id_players(message: Message):
    if str(message.chat.id) != config.ADMIN_ID:
        bot.send_message(message.chat.id, "Вы не являетесь админом", reply_markup=my_marcup.main_menu_marcup())
        return
    mess = []
    for id, nick, status in base.get_all_id_player():
        mess.append(str(id) + "  " + nick + " " + status)
    bot.send_message(message.chat.id, "\n".join(mess), reply_markup=my_marcup.main_menu_marcup())