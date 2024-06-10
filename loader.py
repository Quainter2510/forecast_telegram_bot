from telebot import TeleBot, apihelper
from config_data import config
from database.common import MyDataBase


# apihelper.SESSION_TIME_TO_LIVE = 5 * 60
bot = TeleBot(token=config.BOT_TOKEN)
base = MyDataBase()


