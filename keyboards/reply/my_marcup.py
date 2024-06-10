from telebot import types
from config_data import relations
from loader import base


def main_menu_marcup() -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup()
    marcup.add(types.KeyboardButton("Сделать прогноз"),
               types.KeyboardButton("Изменить прогноз"),
               types.KeyboardButton("Посмотреть итог тура"),
               types.KeyboardButton("Посмотреть турнирную таблицу"),
               types.KeyboardButton("Посмотреть свой прогноз"),
               types.KeyboardButton("Обновить"),
               types.KeyboardButton("Сброс"),
               types.KeyboardButton("Посмотреть прогноз всех участников"))
    return marcup


def tour_menu_marcup() -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.add(types.KeyboardButton("Вернуться в меню"))
    for i in relations.HUMAN_DCT.keys():
        marcup.add(types.KeyboardButton(f"{i}"))
    return marcup


def short_tour_menu_marcup() -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.add(types.KeyboardButton("Вернуться в меню"))
    now_tour = base.get_now_tour()
    min_tour = max(now_tour - 3, 0)
    for i in list(relations.HUMAN_DCT.keys())[min_tour:min(min_tour + 4, max(relations.TOUR_DCT.keys()))]:
        marcup.add(types.KeyboardButton(f"{i}"))
    return marcup


def matches_tour_marcup(mathes) -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.add(types.KeyboardButton("Вернуться в меню"))
    for match in mathes:
        marcup.add(types.KeyboardButton(*match))
    return marcup