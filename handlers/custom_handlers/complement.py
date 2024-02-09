from loader import bot, base
from keyboards.reply import my_marcup
from telebot.types import Message
from config_data import config
from matches_parser import parser

@bot.message_handler(commands=["complement"])
def complement(message: Message) -> None:
    if str(message.chat.id) != config.ADMIN_ID:
        return
    if len(message.text.split()) != 2:
        bot.send_message(message.chat.id, "не указан тур", reply_markup=my_marcup.main_menu_marcup())
        return
    tour = int(message.text.split()[1])
    matches = list(filter(lambda x: x[0] == tour, parser()))
    base.fill_matches(matches)
    base.complement_forecast(matches)