from config_data.config import ADMIN_ID, ADMIN_ID2
from loader import bot, base
import datetime 
import time



def reminder():
    bot.send_message(ADMIN_ID, "reminder start")
    bot.send_message(ADMIN_ID2, "reminder start")
    players = base.reminder(base.get_now_tour())
    for elem in players:
        bot.send_message(elem[0], "Матчи скоро начнутся. Не забудьте сделать прогноз")
        bot.send_message(ADMIN_ID, base.get_nickname_player(elem[0]) + " не сделал прогноз")
        bot.send_message(ADMIN_ID2, base.get_nickname_player(elem[0]) + " не сделал прогноз")
    bot.send_message(ADMIN_ID, "reminder finish")
    bot.send_message(ADMIN_ID2, "reminder finish")

while True:
    if datetime.datetime.now().day in (15, 16, 17, 19, 20, 21, 22) and datetime.datetime.now().hour == 15 or \
        datetime.datetime.now().day in (18, 25, 26, 29, 30, 1, 2, 5, 6) and datetime.datetime.now().hour == 18 or \
        datetime.datetime.now().day in (23, 24, 14, 10, 9) and datetime.datetime.now().hour == 21:
        reminder()
        time.sleep(10)