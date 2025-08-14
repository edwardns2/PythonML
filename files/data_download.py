import pandas as pd
import yfinance as yf

data = yf.download("AAPL", start="1980-01-01")
data.columns = data.columns.get_level_values(0)
data.to_csv("data/aapl.csv")
