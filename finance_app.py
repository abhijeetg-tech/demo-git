import yfinance as yf #yahoofinance
import streamlit as st

# AAPL  → Apple
# MSFT  → Microsoft
# GOOGL → Alphabet (Google)
# AMZN  → Amazon
# META  → Meta (Facebook)
# TSLA  → Tesla
# NFLX  → Netflix
# NVDA  → NVIDIA

comp = st.text_input("Enter Stock Ticker:", "AAPL")
data = yf.Ticker(comp)
df = data.history(start = "2019-01-01", end="2026-01-01")
st.dataframe(df)

st.line_chart(df.Close)
st.bar_chart(df.Volume)