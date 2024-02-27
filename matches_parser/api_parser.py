import requests
from http import HTTPStatus
from pprint import pprint
from helper_function.matches_dict import DataMatch
from config_data.config import API_TOKEN

url = "https://v3.football.api-sports.io/fixtures"

def parse(id_league=2, season=2023):
    tokens = iter([API_TOKEN])
    headers = {
        'x-rapidapi-key': next(tokens),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    payload = {'league': id_league, 'season': season}
    response = requests.request("GET", url, headers=headers, params=payload)
    if response.status_code != HTTPStatus.OK or response.json().get('errors'):
        raise Exception('Pezda parseru')
    response_dict = response.json()
    all_matches = []
    for match in response_dict['response']:
        id_match = match['fixture']['id']
        datetime = match['fixture']['date'] # UTC!!!
        status = match['fixture']['status']['long']
        team_home = match['teams']['home']['name']
        team_away = match['teams']['away']['name']
        goals_home = match['goals']['home']
        goals_away = match['goals']['away']
        round_match = match['league']['round']

        data_match = DataMatch(match_id=id_match,
                               tour=round_match,
                               league_id=id_league,
                               status=status,
                               team_home=team_home,
                               team_away=team_away,
                               goals_home=goals_home,
                               goals_away=goals_away,
                               datetime=datetime)
        all_matches.append(data_match)
    return all_matches

# res = parse()[-1]

# pprint(parse())

