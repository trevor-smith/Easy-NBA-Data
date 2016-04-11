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

    AGENT_DETAILS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64;\
    rv:430) Gecko/20100101'}

    def __init__(self, season='2015-16'):
        self.season = season

    def get_player_ids(season='2015-16', headers=AGENT_DETAILS):
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
            '?IsOnlyCurrentSeason=1&LeagueID=00&Season=%s' % (season)

        response = requests.get(player_ids_url, headers=AGENT_DETAILS)
        response.raise_for_status()

        print 'downloading player ids for season: ' + season

        players = response.json()['resultSets'][0]['rowSet']
        player_ids = {}

        for player in players:
            player_ids[player[2]] = player[0]

        return player_ids

    def game_logs(season='2015-16', players=get_player_ids(), headers=AGENT_DETAILS):
            """Retrieves the game logs for the player list specified.  This will
            return a list of lists of player data.  The default season is
            2015-16 and it retrieves for players active during that season.
            """

            data = []

            for k, v in players.iteritems():
                game_logs_url = 'http://stats.nba.com/stats/playergamelog?' + \
                'LeagueID=00&PlayerID=%s&Season=%s&SeasonType=Regular+Season' \
                % (v, season)
                print 'extracting data for: ' + str(k) + ' ' + str(v)
                print game_logs_url
                response = requests.get(game_logs_url, headers=AGENT_DETAILS)
                results = response.json()['resultSets'][0]['rowSet']
                try:
                    for game in results:
                        data.append(game)
                except:
                    print 'bad request'

            return data

if __name__ == "__main__":
    main()
