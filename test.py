# Here the sinple code for testing our grabbing methods

import api_sports
import sportradar

import json

res = api_sports.general_info_about_player(id="2")
res = api_sports.detailed_player_statistics(id="2", season="2022")
res = api_sports.detailed_team_statistics(id="2", season="2022")
res = api_sports.players_in_team(team="2", season="2022")
res = api_sports.game_events(id="2")
res = api_sports.teams_statistic_in_game(id="1", team="1")

with open("detailed_player_statistics_2_2022.json", "w") as fp:
    json.dump(res,fp) 

res = sportradar.player_info(player_id="0acdcd3b-5442-4311-a139-ae7c506faf88")
res = sportradar.team_info(team_id="4809ecb0-abd3-451d-9c4a-92a90b83ca06")
res = sportradar.game_info(game_id="7d06369a-382a-448a-b295-6da9eab53245")
