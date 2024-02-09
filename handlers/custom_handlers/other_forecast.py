from loader import bot, base
from telebot.types import Message
from keyboards.reply import my_marcup
from helper_function import helper_func
from config_data import config, relations
from image_creator import table_creator

def get_other_forecasts(message: Message):
    if not config.ALL_FUNCTION_READY:
        bot.send_message(message.chat.id, "Функция временно недоступна", reply_markup=my_marcup.main_menu_marcup())
        return
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.send_message(message.chat.id, "Тур указан неверно")
        bot.register_next_step_handler(message, get_other_forecasts)
        return
    tour = relations.HUMAN_DCT[message.text]
    if base.get_now_tour() < tour:
        bot.send_message(message.chat.id, "Дождитесь начала тура", reply_markup=my_marcup.main_menu_marcup())
        return
    
    players = base.get_all_id_player()
    for id, nickname, status in players:
        res = base.get_result_tour(tour)
        points = 0
        data = []
        for match, result in res:
            self_res = base.get_other_forecast_match(id, match)
            points += helper_func.counting_of_points(result, self_res)
            data.append([match, result, self_res, helper_func.counting_of_points(result, self_res)])
        table_creator.result_tour(data, message.text, points, nickname)
        img = open("images/ready_tables/result_tour.png", 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=my_marcup.main_menu_marcup())