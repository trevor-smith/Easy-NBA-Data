# Easy NBA Data
This repository provides easy access of NBA.com data.  This will start off initially as game log data, but will expand to include more advanced statistics also housed on the NBA.com website

# Current Status
This currently supports game logs only.  There is also an issue when creating the historical data object.  The object initializes fine, but accessing the player_ids and game_logs attributes do not happen properly.  However, if you define these functions separately, they appear to work

# Example
```python
import historical_data

season_2015 = historical_data.HistoricalData(season='2015-16')
player_ids = season_2015.get_player_ids()
data_2015 = season_2015(players=player_ids)
```


