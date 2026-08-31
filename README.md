# ALPACA-TRADING-RIDICULOUS-FEATURES

Building a model using Python to predict the stock market in an attempt to beat the S&P 500 using absolutely ridiculous features

## Feature scrapers

Each script scrapes one "ridiculous feature" that might (probably won't) correlate with the market.

| Script | Feature | Source | Output |
| --- | --- | --- | --- |
| `ford-recalls.py` | Ford recall severity, subject, component and date, 1966–2026 | vehiclesafetyrecalls.com | `data/ford-recalls.csv` |
| `birdcast.py` | Nightly peak bird migration traffic and location for Wisconsin | dashboard.birdcast.org | in-memory (WIP) |

### `ford-recalls.py`

Loops over model years 1966–2026, parses each year's Ford Motor Company recall
listing with BeautifulSoup, concatenates the results into one DataFrame,
converts the recall date to a datetime, and writes `data/ford-recalls.csv`.

### `birdcast.py`

Pulls a single BirdCast dashboard night for region `US-WI` and extracts the peak
migration traffic count and location. Still a work in progress — the night is
currently hard-coded and nothing is written to disk yet.

## Usage

```bash
python -m venv venv
venv\Scripts\activate        # Windows; use source venv/bin/activate elsewhere
pip install pandas requests beautifulsoup4

python ford-recalls.py
python birdcast.py
```

`ford-recalls.py` expects a `data/` directory to exist before it runs.

## Dependencies

- pandas
- requests
- beautifulsoup4
