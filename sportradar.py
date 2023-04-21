import requests

############
# SPORTRADAR
# NFL
# DOCS: https://developer.sportradar.com/docs/read/american_football/NFL_v7#game-statistics
############
api_key = "831eb8b9f6ca03b6aa6391b978edd7d4" # NFL Trial Key
base_url = "https://v1.american-football.api-sports.io" #NFL 
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