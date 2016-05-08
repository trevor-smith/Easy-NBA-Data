import sys
import requests
import pandas as pd
import numpy as np

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

    global AGENT_DETAILS

    AGENT_DETAILS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
                     'referer': 'http://stats.nba.com/scores/'
                    }

    def __init__(self, season='2015-16', headers=AGENT_DETAILS):
        self.season = season
        self.headers = headers

    def get_player_ids(self):
        """This function returns a dictionary of player names and
        player ids.  The default season is 2015/2016.

        Ex: '{'Quincy Acy': 203112,
              'Steven Adams': 203500}

        Change Season:
                season: specify 'yyyy-yy' format.  The four digit year is the
                start of the season.  The two digit year is the end of the
                season.  Ex: '2014-15' is the 2014/2015 season.
        """

        player_ids_url = 'http://stats.nba.com/stats/commonallplayers' + \
            '?IsOnlyCurrentSeason=1&LeagueID=00&Season=%s' % (self.season)

        response = requests.get(player_ids_url, headers = self.headers)
        response.raise_for_status()

        players = response.json()['resultSets'][0]['rowSet']
        player_ids = {}

        for player in players:
            player_ids[player[2]] = player[0]

        return player_ids

    def game_logs(self):
            """Retrieves the game logs for the player list specified.  This will
            return a list of lists of player data.  The default season is
            2015-16 and it retrieves for players active during that season.
            """

            players = self.get_player_ids()
            data = []

            for k, v in players.iteritems():
                game_logs_url = 'http://stats.nba.com/stats/playergamelog?' + \
                'LeagueID=00&PlayerID=%s&Season=%s&SeasonType=Regular+Season' \
                % (v, self.season)

                response = requests.get(game_logs_url, headers = self.headers)
                results = response.json()['resultSets'][0]['rowSet']
                try:
                    for game in results:
                        data.append(game)
                except:
                    print 'bad request'

            return data
            
def main():
    pass

def main():
    pass

if __name__ == '__main__':
    main()
