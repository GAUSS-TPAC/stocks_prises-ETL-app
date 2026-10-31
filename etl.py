"""Minimal stock-price ETL: fetch quotes from Finnhub and append them to a CSV.

Set your Finnhub API key in the environment before running:
    export FINNHUB_API_KEY="your_key"
"""
import os
import time

import pandas as pd
import requests

API_KEY = os.environ.get("FINNHUB_API_KEY")
if not API_KEY:
    raise SystemExit("Set FINNHUB_API_KEY in your environment (get one at https://finnhub.io).")

# Output file next to this script (override with STOCK_CSV).
CSV_PATH = os.environ.get(
    "STOCK_CSV", os.path.join(os.path.dirname(os.path.abspath(__file__)), "stock_prises.csv")
)

TICKERS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "UNH"]

rows = {"stock name": [], "current price": [], "time": []}
for ticker in TICKERS:
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={API_KEY}"
    data = requests.get(url, timeout=10).json()
    rows["stock name"].append(ticker)
    rows["current price"].append(data["c"])
    rows["time"].append(time.time())

df = pd.DataFrame.from_dict(rows)
write_header = not os.path.isfile(CSV_PATH)
df.to_csv(CSV_PATH, mode="a", header=write_header, index=False)
print(f"Appended {len(df)} rows to {CSV_PATH}")
