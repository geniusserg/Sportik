import requests

############
# SPORTRADAR
# NFL
# DOCS: https://developer.sportradar.com/docs/read/american_football/NFL_v7#game-statistics
############
api_key = "uznza83sc2cquqsfg933tuc2" # NFL Trial Key
base_url = "https://api.sportradar.us" #NFL 
locale = "en"

def player_info(player_id:str)->dict:
    url = f"{base_url}/nfl/official/trial/v7/{locale}/players/{player_id}/profile.json?api_key={api_key}"
    return requests.get(url).json()

def team_info(team_id:str)->dict:
    url = f"{base_url}/nfl/official/trial/v7/{locale}/teams/{team_id}/profile.json?api_key={api_key}"
    return requests.get(url).json()

def game_info(game_id:str)->dict:
    url = f"{base_url}/nfl/official/trial/v7/{locale}/games/{game_id}/statistics.json?api_key={api_key}"
    return requests.get(url).json()

def season_schedule(season_year:str)->dict:
    url = f"{base_url}/nfl/official/trial/v7/{locale}/games/{season_year}/reg/schedule.json?api_key={api_key}"
    return requests.get(url).json()
