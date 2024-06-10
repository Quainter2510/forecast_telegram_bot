from telebot import TeleBot, apihelper
from config_data import config
from database.common import MyDataBase
import schedule
from handlers.custom_handlers import reminder

# Define a function to print a message



# Schedule the task to run every day at 7:00 AM
schedule.every().minute.do(reminder)


# apihelper.SESSION_TIME_TO_LIVE = 5 * 60
bot = TeleBot(token=config.BOT_TOKEN)
base = MyDataBase()


