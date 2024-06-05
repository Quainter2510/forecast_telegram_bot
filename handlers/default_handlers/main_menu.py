from loader import bot
from keyboards.reply.my_marcup import short_tour_menu_marcup, main_menu_marcup
from handlers.custom_handlers.set_tour_forecast import *
from handlers.custom_handlers.set_goleador import *
from handlers.custom_handlers.change_match_forecast import *
from handlers.custom_handlers.get_result_tour import *
from handlers.custom_handlers.get_my_forecast import *
from handlers.custom_handlers.get_main_table import check_result_tournament
from handlers.custom_handlers.other_forecast import *
from handlers.custom_handlers.update import *

def ask_tour(message, func):
    bot.send_message(message.chat.id, "Выберите тур", 
                    reply_markup=short_tour_menu_marcup())
    bot.register_next_step_handler(message, func)


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == "Сделать прогноз":
        ask_tour(message, set_tour_forecast)
    elif message.text == "Изменить прогноз":
        ask_tour(message, change_choice_tour)
    elif message.text == "Посмотреть итог тура":
        ask_tour(message, check_result_tour)
    elif message.text == "Посмотреть свой прогноз":
        ask_tour(message, check_forecast_tour)
    elif message.text == "Посмотреть прогноз всех участников":
        ask_tour(message, get_other_forecasts)
    elif message.text == "Обновить":
        update(message)
    elif message.text == "Чемпион+бомбардир":
        if config.REGISTRATION_IS_OPEN:
            bot.send_message(message.chat.id, "Напишите чемпиона")
            bot.register_next_step_handler(message, set_champ)
        else:
            show_goleador_list(message.chat.id)
    elif message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=main_menu_marcup())
    else:
        bot.send_message(message.chat.id, "Неизвестная команда", reply_markup=main_menu_marcup())