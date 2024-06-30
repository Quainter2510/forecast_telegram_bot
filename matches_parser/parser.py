import requests
from bs4 import BeautifulSoup
from helper_function.datetime_func import datetime_transform
from helper_function.helper_func import get_match_status
from config_data import config
import pprint
from itertools import groupby

overwrite = {'* * Англия—Словакия': ["Англия—Словакия", "1:1"]}


def parser():
    response = requests.get(config.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find('div', class_="cal_sort_tour").find_all("div")
    res = []
    tour = 0
    last = None
    for i, quote in enumerate(quotes):
        
        datetime = quote.find_all("li")[0].text
        match = quote.find_all("li")[1].text
        result = quote.find_all("a")[0].text



        if match in overwrite:
            result = overwrite[match][1]
            match = overwrite[match][0]

        datetime = datetime_transform(datetime)
        status = get_match_status(datetime)
        res.append((datetime, match, result, status))

    res.sort()
    ress = []
    for elem in res:
        if elem[0].split()[0] != last:
            tour += 1
            last = elem[0].split()[0]
        ress.append((tour, *elem))
    pprint.pprint(ress)

    return ress