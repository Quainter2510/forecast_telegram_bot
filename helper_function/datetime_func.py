from datetime import *

def date_transform(datetr: str) -> str:
    d = list(map(int, reversed(datetr.split('/'))))
    d = date(*d)
    return d.strftime("%Y-%m-%d")


def datetime_transform(dt: str) -> str:
    date, time = dt.split()
    date = date_transform(date)
    # time = "00:00" if time == 'ок' else time
    return date + ' ' + time