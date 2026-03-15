import os
import requests
import time
import pandas as pd

add_header=True
create_header= not os.path.isfile('/home/gauss/Bureau/learndev/ML/ETL app/stock_prises.csv')
api_key = 'd6mr7jhr01qir35i5hdgd6mr7jhr01qir35i5he0'

data_dictionary ={'stock name': [],
                  'current price': [], 
                  'time':[]
                  }

tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 'V', 'UNH']

for ticker in tickers:
    url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}'
    
    response = requests.get(url)
    data = response.json()

    data_dictionary['stock name'].append(ticker)
    data_dictionary['current price'].append(data['c'])
    data_dictionary['time'].append(time.time())

df = pd.DataFrame.from_dict(data_dictionary)
df.to_csv('/home/gauss/Bureau/learndev/ML/ETL app/stock_prises.csv',mode='a', header= create_header, index=False)
    

