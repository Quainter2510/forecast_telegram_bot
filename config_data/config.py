import os
from dotenv import load_dotenv, find_dotenv
from config_data.load_settings import load

if not find_dotenv():
    print("not found .env")
else:
    load_dotenv()

ALL_FUNCTION_READY = None 
REGISTRATION_IS_OPEN = None 
load()

BOT_TOKEN=os.getenv("MAIN_BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
API_TOKEN = os.getenv("API_TOKEN")

NUMBER_OF_TOUR = 8
SUM_COLUMN = 3
NUMBER_OF_PLAYERS = 7
COUNT_MATCHES_IN_TOUR = 4
TOUR1_COLUMN = 4
NICKNAME_COLUMN = 0 
START_SHOW_TOUR_COLUMN = 4
COUNT_TOUR_IN_TABLE = 8

image_width = 1280
image_height = 720

 
POSSIBLE_STATUSSES = ["superadmin", "admin", "player", "owe"]

start_info_msg = """Для участия необходимо перевести 1200 рублей Александрову Павлу на номер 89205450183 (сбер) с указанием никнейма в комментарии. После подтверждения перевода вы будете добавлены в турнир."""

URL = 'https://www.livecup.run/football/champions-league/calendar-playoff/'
