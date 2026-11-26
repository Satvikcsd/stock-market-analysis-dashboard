"""Downloading stock price data."""

import pandas as pd
import yfinance as yf


def load_prices(symbol: str, period: str) -> pd.DataFrame:
    """Download daily prices for a ticker from Yahoo Finance.

    Returns a DataFrame indexed by date with Open, High, Low, Close and
    Volume columns. The DataFrame is empty if the ticker is not found.
    """
    df = yf.download(symbol, period=period, auto_adjust=True, progress=False)

    # Newer yfinance versions return two-level column names; flatten them.
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df
