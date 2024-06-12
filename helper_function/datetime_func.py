from datetime import *

def date_transform(datetr: str) -> str:
    d = list(map(int, reversed(datetr.split('/'))))
    d = date(*d)
    return d.strftime("%Y-%m-%d")


def datetime_transform(dt: str) -> str:
    dt = dt.split()
    date = dt[0]
    time = " ".join(dt[1:])
    date = date_transform(date)
    # time = "00:00" if time == 'ок' else time
    return date + ' ' + time