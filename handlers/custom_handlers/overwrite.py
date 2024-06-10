from loader import bot, base
from keyboards.reply import my_marcup
from telebot.types import Message
from config_data import config
from matches_parser import parser

@bot.message_handler(commands=["overwrite"])
def complement(message: Message) -> None:
    if str(message.chat.id) not in (config.ADMIN_ID, config.ADMIN_ID2):
        return
    base.overwrite_matches()