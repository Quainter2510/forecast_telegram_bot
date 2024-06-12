from loader import bot, base
from keyboards.reply import my_marcup
from config_data import config
from telebot.types import Message


@bot.message_handler(commands=["set_status"])
def get_id(message: Message):
    if str(message.chat.id) != config.ADMIN_ID:
        bot.send_message(message.chat.id, "Вы не являетесь админом", reply_markup=my_marcup.main_menu_marcup())
        return
    mess = message.text.split()
    if len(mess) != 3:
        bot.send_message(message.chat.id, "/set_status <id> <status>", reply_markup=my_marcup.main_menu_marcup())
        bot.send_message(message.chat.id, "statusses:\n" + "\n".join(config.POSSIBLE_STATUSSES), reply_markup=my_marcup.main_menu_marcup())
        return
    
    if base.set_status(mess[1], mess[2]):
        bot.send_message(message.chat.id, "Статус изменен", reply_markup=my_marcup.main_menu_marcup())
    else:
        bot.send_message(message.chat.id, "Произошла ошибка", reply_markup=my_marcup.main_menu_marcup())

