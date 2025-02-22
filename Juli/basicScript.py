import yfinance as yf
import pandas as pd

ticker = 'MSFT'
data = yf.download(ticker,start='2020-01-01',end='2025-01-01',interval='1d')

print(data['Low'])


