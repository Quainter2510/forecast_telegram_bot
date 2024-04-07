from loader import bot, base
from config_data import config
from telebot.types import Message 
from keyboards.reply import my_marcup


@bot.message_handler(commands=["start"])
def start(message: Message):
    if base.check_user_in_tournament(message.chat.id):
        bot.send_message(message.chat.id, "Вы уже зарегистрированы в турнире",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if not config.REGISTRATION_IS_OPEN:
        bot.send_message(message.chat.id, "Вы не можете принять участие в турнире")
        return
    bot.send_message(message.chat.id, "Введите имя, которое будет выводиться в таблицу")
    bot.register_next_step_handler(message, set_nickname)

def set_nickname(message: Message):
    bot.send_message(message.chat.id, config.start_info_msg)
    bot.send_message(config.ADMIN_ID, "Присоединился " + str(message.chat.id) + " " + message.text)
    bot.send_message(config.ADMIN_ID, f"Присоединился {message.chat.id} {message.text}")

    user_id = message.chat.id
    user_nickname = message.text


    try:
        base.add_user(user_id, user_nickname)
    except:
        print()

        
    bot.send_message(user_id, "Вы зарегистрированы в турнире",
                reply_markup=my_marcup.main_menu_marcup())

    




