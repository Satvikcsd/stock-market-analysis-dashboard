"""Calculations on a series of closing prices."""

import pandas as pd

TRADING_DAYS = 252


def daily_returns(close: pd.Series) -> pd.Series:
    """Percentage change from one day to the next."""
    return close.pct_change().dropna()


def total_return(close: pd.Series) -> float:
    """Return over the whole period, in percent."""
    return (close.iloc[-1] / close.iloc[0] - 1) * 100


def annual_volatility(returns: pd.Series) -> float:
    """Standard deviation of daily returns, scaled to a year, in percent."""
    return returns.std() * (TRADING_DAYS ** 0.5) * 100


def drawdown(close: pd.Series) -> pd.Series:
    """Fall from the highest price so far, as a fraction (0 to -1)."""
    return close / close.cummax() - 1


def max_drawdown(close: pd.Series) -> float:
    """Largest fall from a previous peak, in percent."""
    return drawdown(close).min() * 100


def moving_average(close: pd.Series, window: int) -> pd.Series:
    """Average closing price over the last `window` days."""
    return close.rolling(window).mean()


def rsi(close: pd.Series, window: int = 14) -> pd.Series:
    """Relative Strength Index on a scale of 0 to 100."""
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(window).mean()
    loss = (-delta.clip(upper=0)).rolling(window).mean()
    return 100 - 100 / (1 + gain / loss)
