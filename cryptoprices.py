from datetime import datetime, timedelta
import requests
import pandas as pd

# List of cryptos we want to get:
cryptos = ['BTC', 'ETH', 'XTZ', 'RVN']

for crypto in cryptos:
    # Get the data from the yahoo API
    url = f'https://finance.yahoo.com/quote/{crypto}-USD/history?period1=1609459200&period2=1640908800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
    # Set the header so we actually get a response
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    text = response.text
    data = text.split('"HistoricalPriceStore":{"prices":')[1].split(',"isPending"')[0]
    df = pd.read_json(data)
    df['date'] = pd.to_datetime(df['date'], unit='s')
    df.set_index('date', inplace=True)
    df.to_excel(f'{crypto}_prices.excel')
