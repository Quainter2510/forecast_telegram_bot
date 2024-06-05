from loader import bot, base
from keyboards.reply import my_marcup
from config_data import relations
from helper_function import helper_func
from telebot.types import Message



def show_goleador_list(id: int):
    msg = 'Список прогнозов: \n'
    for num, player in enumerate(base.get_all_id_player(), start=1):
        msg += f"{num} {base.get_nickname_player(player)}: {base.get_champ(player)} | {base.get_goleador(player)}"
    bot.send_message(id, msg)


def set_champ(message: Message) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    base.set_champ(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Введите бомбардира")
    bot.register_next_step_handler(message, set_goleador)

def set_goleador(message: Message) -> None:
    base.set_goleador(message.chat.id, message.text)
    bot.send_message(message.chat.id, f"Вы выбрали победителя - {base.get_champ(message.chat.id)}")
    bot.send_message(message.chat.id, f"Вы выбрали бомбардира - {base.get_goleador(message.chat.id)}")