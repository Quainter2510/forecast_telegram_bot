from loader import bot, base
from keyboards.reply import my_marcup
from config_data import config, relations
from telebot.types import Message
from helper_function import helper_func
from image_creator import table_creator



def check_result_tour(message: Message):
    if not config.ALL_FUNCTION_READY:
        bot.send_message(message.chat.id, "Функция временно недоступна", reply_markup=my_marcup.main_menu_marcup())
        return

    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.send_message(message.chat.id, "Тур указан неверно")
        bot.register_next_step_handler(message, check_result_tour)
        return
    res = base.get_result_tour(relations.HUMAN_DCT[message.text])
    points = 0
    data = []
    currtour = relations.HUMAN_DCT[message.text]
    for match, res, status in res:
        self_res = base.get_forecast_match(message.chat.id, match)
        points += helper_func.counting_of_points(res, self_res)
        data.append([match, res, self_res, helper_func.counting_of_points(res, self_res), status])
    table_creator.result_tour(data, message.text, points)
    img = open("images/ready_tables/result_tour.png", 'rb')
    bot.send_photo(message.chat.id, img, reply_markup=my_marcup.main_menu_marcup())

    table_creator.points_tour(base.get_points_of_tour(relations.TOUR_DCT[currtour]), base.tour_in_process(relations.HUMAN_DCT[message.text]))
    img = open("images/ready_tables/points_tour.png", 'rb')
    bot.send_photo(message.chat.id, img, reply_markup=my_marcup.main_menu_marcup())