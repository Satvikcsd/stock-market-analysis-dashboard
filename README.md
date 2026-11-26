# Stock Market Analysis Dashboard

An interactive dashboard that downloads historical stock prices and turns
them into simple, readable charts and risk numbers. Type a ticker symbol,
pick a time period, and the dashboard updates straight away.

## Features

- Search any ticker supported by Yahoo Finance, including Indian stocks
  (for example `TCS.NS`, `INFY.NS`) and US stocks (for example `AAPL`)
- Choose a time period of 6 months, 1 year, 2 years or 5 years
- Price chart with two moving averages whose window sizes you control
  with sliders
- RSI (14-day) chart with the 30 and 70 reference lines
- Histogram of daily returns
- Summary numbers: last close, return over the period, annualised
  volatility and maximum drawdown

## Tech stack

- Python 3.12
- Streamlit for the web interface
- yfinance for downloading price data
- pandas for the calculations
- matplotlib for the charts

## How to run

    cd market-analysis
    py -3.12 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    streamlit run app.py

Then open http://localhost:8501 in your browser.

## How the numbers are calculated

| Measure | Meaning |
|---|---|
| Return over period | Last close divided by first close, minus 1 |
| Annualised volatility | Standard deviation of daily returns times the square root of 252 trading days |
| Maximum drawdown | Largest fall from a previous peak to a later low |
| RSI (14-day) | Average gain divided by average loss over 14 days, scaled to 0 to 100 |
| Moving average | Average closing price over the chosen number of days |

## Project structure

    market-analysis/
    ├── app.py
    ├── requirements.txt
    └── README.md

## Notes

- Data comes from Yahoo Finance and may be delayed or occasionally
  incomplete.
- If a ticker returns no data, check the symbol. Indian stocks need
  `.NS` (NSE) or `.BO` (BSE) at the end.
- This project is for learning only and is not financial advice.

## Author

Jagannath
B.E. Computer Science & Engineering (Design), graduating 2027
