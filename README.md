# stock-prices ETL

![Python](https://img.shields.io/badge/Python-3776ab)
![Finnhub](https://img.shields.io/badge/API-Finnhub-1a7f64)
![pandas](https://img.shields.io/badge/pandas-150458)

A tiny **ETL script** that fetches real-time stock quotes from the [Finnhub](https://finnhub.io) API for a list of tickers and appends them, with a timestamp, to a CSV — a minimal, readable example of an *extract → transform → load* loop.

## What it does

- **Extract**: queries Finnhub `/quote` for each ticker (AAPL, GOOGL, MSFT, AMZN, TSLA, META, NVDA, JPM, V, UNH).
- **Transform**: keeps the current price and the capture time.
- **Load**: appends the rows to `stock_prises.csv` (writes the header only on first run).

Run it on a schedule (cron) to build a time series of prices.

## Run

```bash
git clone https://github.com/GAUSS-TPAC/stocks_prises-ETL-app.git
cd stocks_prises-ETL-app
pip install requests pandas
export FINNHUB_API_KEY="your_key"      # free key at https://finnhub.io
python etl.py
```

| Variable | Purpose | Default |
|---|---|---|
| `FINNHUB_API_KEY` | Finnhub API key (required) | — |
| `STOCK_CSV` | Output CSV path | `stock_prises.csv` next to the script |

### Example: run every minute with cron

```cron
* * * * * FINNHUB_API_KEY=your_key /usr/bin/python3 /path/to/etl.py
```

## License

MIT.
