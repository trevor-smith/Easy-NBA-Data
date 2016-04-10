import requests
import pandas as pd
import numpy as np

player_ids_url = 'http://stats.nba.com/stats/commonallplayers' + \
            '?IsOnlyCurrentSeason=1&LeagueID=00&Season=2015-16'

class HistoricalData():
    """Retrieves historical data from NBA.com for a specified player and
    season.  By default any function in this class will grab all player
    data from the '2015-16' season.

    Attributes:
        game_logs: historical game log data

    Change Player or Season:
        player: specify python list of valid player ids
        season: specify 'yyyy-yy' format.  The four digit year is the
                start of the season.  The two digit year is the end of the
                season.  Ex: '2014-15' is the 2014/2015 season.
    """

    def __init__(self, players, season='2015-16'):
        self.players = players
        self.season = season

    def game_logs()

# request the URL and parse the JSON
response = requests.get(player_ids_url)
response.raise_for_status() # raise exception if invalid response
player_ids = response.json()['resultSets'][0]['rowSet']

player_lookup = []
for player in player_ids:
    player_lookup.append([player[7], player[2]])

def game_logs(player_id, season='2015-16'):
    url = 'http://stats.nba.com/stats/playergamelog?LeagueID=00&' + \
            'PlayerID=%s&Season=%s&SeasonType=Regular+Season' \
            % (player_id, season)
    return url

headers = response.json()['resultSets'][0]['headers']

data = []
bad_ids = []
for i in player_lookup[:2]:
    pid = i[0]
    try:
        response = requests.get(game_logs(pid))
        results = response.json()['resultSets'][0]['rowSet']
        for row in results:
            data.append(row)
    except:
        print 'bad request: ' + str(pid)
        bad_ids.append(pid)
