from loader import bot, base
from keyboards.reply import my_marcup
from config_data import relations
from helper_function import helper_func
from telebot.types import Message


def check_forecast_tour(message: Message) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.send_message(message.chat.id, "Тур указан неверно")
        bot.register_next_step_handler(message, check_forecast_tour)
        return
    output_forecast(relations.HUMAN_DCT[message.text], message.chat.id)

def output_forecast(selected_tour: int, id: int) -> None:
    ans = f"Ваш прогноз на {selected_tour} тур :\n\n"
    res = base.get_forecast_tour(id, selected_tour)
    for match in res:
        name = match.split("—")
        ans += name[0] + " " + name[2] + " " + name[1] + '\n'
    bot.send_message(id, ans, reply_markup=my_marcup.main_menu_marcup())