import requests
from bs4 import BeautifulSoup
from helper_function.datetime_func import *
from config_data import config, relations
from pprint import pprint


def parser():
    response = requests.get(config.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find('div', class_="cal_sort_tour").find_all("div")
    res = []
    for i, quote in enumerate(quotes):
        quote1 = quote.find_all("li")
        quote2 = quote.find_all("a")
        dt = datetime_transform(quote1[0].text)
        res.append([i // config.COUNT_MATCHES_IN_TOUR + 1, dt, quote1[1].text, quote2[0].text])
    pprint(res)
    return res

