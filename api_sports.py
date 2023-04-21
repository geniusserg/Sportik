import requests

#NFL
api_key = "831eb8b9f6ca03b6aa6391b978edd7d4" # NFL Trial Key
base_url = "https://v1.american-football.api-sports.io" #NFL 
headers = {
    'x-apisports-key': api_key
}

def general_info_about_player(id: str)->dict:
    url = f"{base_url}/players?id={id}"
    return requests.get(url, headers=headers).json()

def detailed_player_statistics(id: str, season:str)->dict:
    url = f"{base_url}/players/statistics?id={id}&season={season}"
    return requests.get(url, headers=headers).json()

def detailed_team_statistics(id:str, season:str)->dict:
    url = f"{base_url}/players/statistics?team={id}&season={season}"
    return requests.get(url, headers=headers).json()

def players_in_team(team:str, season:str)->dict:
    url = f"{base_url}/players?team={team}&season={season}"
    return requests.get(url, headers=headers).json()

def general_team_info(team:str)->dict:
    url = f"{base_url}/teams?id={team}"
    return requests.get(url, headers=headers).json()

def games(id:str=None, team:str=None, date:str=None, live:str=None):
    url = None
    if (id != None):
        url = f"{base_url}/games?id={live}"
    elif (team != None):
        url = f"{base_url}/games?team={team}"
    elif (live != None):
        url = f"{base_url}/games?live={live}"
    elif (date != None):
        url = f"{base_url}/games?date={date}"
    else:
        raise Exception("At least one parameter should be defined!")
    return requests.get(url, headers=headers).json()

def game_events(id:str)->dict:
    url = f"{base_url}/games/events?id={id}"
    return requests.get(url, headers=headers).json()

def teams_statistic_in_game(id:str, team:str)->dict:
    url = f"{base_url}/games/statistics/teams?id={id}&team={team}"
    return requests.get(url, headers=headers).json()

# we can take one player or the whole team
def player_statistic_in_game(id:str, team:str, player:str)->dict:
    url = f"{base_url}/games/statistics/players?id={id}&team={team}&player={player}"
    return requests.get(url, headers=headers).json()
