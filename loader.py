from telebot import TeleBot, apihelper
from config_data import config
from database.common import MyDataBase
from handlers.custom_handlers.reminders import reminder


# apihelper.SESSION_TIME_TO_LIVE = 5 * 60
bot = TeleBot(token=config.BOT_TOKEN)
base = MyDataBase()

reminder()

# handlers.custom_handlers.reminder.reminder()


