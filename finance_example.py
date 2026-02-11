import yfinance as yf #yahoofinance
 
# AAPL  → Apple
# MSFT  → Microsoft
# GOOGL → Alphabet (Google)
# AMZN  → Amazon
# META  → Meta (Facebook)
# TSLA  → Tesla
# NFLX  → Netflix
# NVDA  → NVIDIA

comp = 'AAPL'
data = yf.Ticker(comp)
df = data.history(start = "2019-01-01", end="2023-01-01")