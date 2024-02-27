from typing import TypedDict

class DataMatch(TypedDict):
    match_id: int
    tour: str
    league_id: int
    status: str
    team_home: str
    team_away: str
    goals_home: int | None
    goals_away: int | None
    datetime: str # ?


class DataForecast(TypedDict):
    id: int
    match_id: int
    user_id: int
    goals_home_predict: int | None
    goals_away_predict: int | None
    match_point: int


class DataUser(TypedDict):
    telegram_id: int
    username: str
    status: str
    points_sum: int