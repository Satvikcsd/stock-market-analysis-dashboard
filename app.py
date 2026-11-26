"""Streamlit page: user interface only."""

import matplotlib.pyplot as plt
import streamlit as st

import analysis
from data import load_prices

st.set_page_config(page_title="Market Analysis", layout="wide")
st.title("Stock Market Analysis Dashboard")

# ---------- Sidebar inputs ----------
ticker = st.sidebar.text_input("Ticker symbol", "RELIANCE.NS").upper()
period = st.sidebar.selectbox("Period", ["6mo", "1y", "2y", "5y"], index=1)
short_w = st.sidebar.slider("Short moving average (days)", 5, 50, 20)
long_w = st.sidebar.slider("Long moving average (days)", 20, 200, 50)


@st.cache_data
def get_data(symbol, period):
    return load_prices(symbol, period)


df = get_data(ticker, period)

if df.empty:
    st.error("No data found. Check the ticker symbol (Indian stocks end with .NS, e.g. TCS.NS).")
    st.stop()

close = df["Close"]
returns = analysis.daily_returns(close)

# ---------- Metrics row ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Last close", f"{close.iloc[-1]:,.2f}")
c2.metric("Return over period", f"{analysis.total_return(close):.1f}%")
c3.metric("Annualised volatility", f"{analysis.annual_volatility(returns):.1f}%")
c4.metric("Max drawdown", f"{analysis.max_drawdown(close):.1f}%")

# ---------- Price chart with moving averages ----------
st.subheader("Price and moving averages")
fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(close.index, close, label="Close", linewidth=1.2)
ax.plot(close.index, analysis.moving_average(close, short_w), label=f"{short_w}-day MA")
ax.plot(close.index, analysis.moving_average(close, long_w), label=f"{long_w}-day MA")
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

# ---------- RSI and return distribution ----------
left, right = st.columns(2)

with left:
    st.subheader("RSI (14-day)")
    rsi_values = analysis.rsi(close)
    fig2, ax2 = plt.subplots(figsize=(6, 3))
    ax2.plot(rsi_values.index, rsi_values)
    ax2.axhline(70, linestyle="--", color="red")
    ax2.axhline(30, linestyle="--", color="green")
    ax2.set_ylim(0, 100)
    st.pyplot(fig2)

with right:
    st.subheader("Daily return distribution")
    fig3, ax3 = plt.subplots(figsize=(6, 3))
    ax3.hist(returns * 100, bins=40)
    ax3.set_xlabel("Daily return (%)")
    st.pyplot(fig3)

st.caption("For learning only. This is not financial advice.")
