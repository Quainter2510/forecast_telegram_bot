import os
from dotenv import load_dotenv, find_dotenv
from config_data.load_settings import load

if not find_dotenv():
    print("not found .env")
else:
    load_dotenv()

ALL_FUNCTION_READY = None 
load()

BOT_TOKEN=os.getenv("TEST_BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

NUMBER_OF_TOUR = 30
SUM_COLUMN = 33
NUMBER_OF_PLAYERS = 14
COUNT_MATCHES_IN_TOUR = 8
TOUR1_COLUMN = 3
NICKNAME_COLUMN = 0 
START_SHOW_TOUR_COLUMN = 3
COUNT_TOUR_IN_TABLE = 15
 

start_info_msg = """Для участия необходимо перевести 1200 рублей Александрову Павлу на номер 89205450183 (сбер) с указанием никнейма в комментарии. После подтверждения перевода вы будете добавлены в турнир."""

URL = 'https://www.livecup.run/football/russia/premier-league/calendar-tour/'
