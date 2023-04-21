# Here the sinple code for testing our grabbing methods

import api_sports
import json

res = api_sports.detailed_player_statistics("2", "2022")

with open("detailed_player_statistics_2_2022.json", "w") as fp:
    json.dump(res,fp) 