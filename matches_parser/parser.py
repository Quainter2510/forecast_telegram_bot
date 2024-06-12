import requests
from bs4 import BeautifulSoup
from helper_function.datetime_func import datetime_transform
from helper_function.helper_func import get_match_status
from config_data import config

overwrite = {"* * Арсенал Лондон—Порту": ("Арсенал Лондон—Порту", "1:0"),
             "* * Атлетико—Интер": ("Атлетико—Интер", "2:1"),
             "Манчестер Сити—Реал Мадрид": ("Манчестер Сити—Реал Мадрид", "1:1")}


def parser():
    response = requests.get(config.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find('div', class_="cal_sort_tour").find_all("div")
    res = []
    for i, quote in enumerate(quotes):
        datetime = quote.find_all("li")[0].text
        match = quote.find_all("li")[1].text
        result = quote.find_all("a")[0].text

        if match in overwrite:
            result = overwrite[match][1]
            match = overwrite[match][0]

        datetime = datetime_transform(datetime)
        status = get_match_status(datetime)
        res.append((i // config.COUNT_MATCHES_IN_TOUR + 1, datetime, match, result, status))
    return res