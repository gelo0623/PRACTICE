import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app
#You cann add cool stuff here
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
