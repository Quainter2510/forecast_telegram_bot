from loader import bot, base
from telebot.types import Message
from keyboards.reply import my_marcup
from config_data import config


@bot.message_handler(commands=["update"])
def update(message: Message):
    # if not config.ALL_FUNCTION_READY:
    #     bot.send_message(message.chat.id, "Функция временно недоступна", reply_markup=my_marcup.main_menu_marcup())
    #     return
    currtour = base.get_now_tour()
    base.update_result_tour()
    for id, nickname, status in base.get_all_id_player():
        base.update_tournament_table(id, currtour - 1, base.number_of_points_per_tour(id, currtour - 1))
        base.update_tournament_table(id, currtour, base.number_of_points_per_tour(id, currtour))

    bot.send_message(message.chat.id, "Таблица успешно обновлена", reply_markup=my_marcup.main_menu_marcup())