from yahoo_fin import stock_info as si
from datetime import date, datetime
import pandas as pd

# gainer
si_day_gainer = si.get_day_gainers()
si_day_gainer['day_gainer'] = 'day_gainer'
si_day_gainer['modified_date'] = datetime.today().strftime('%Y-%m-%d')
si_day_gainer.to_csv('data/day_gainer/day_gainer_'+datetime.today().strftime('%Y-%m-%d')+'.csv')

# loser
si_day_loser = si.get_day_losers()
si_day_loser['day_loser'] = 'day_loser'
si_day_loser['modified_date'] = datetime.today().strftime('%Y-%m-%d')
si_day_loser.to_csv('data/day_loser/day_loser_'+datetime.today().strftime('%Y-%m-%d')+'.csv')
