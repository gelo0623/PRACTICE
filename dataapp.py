import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# 1 title
# title screen
st.title("Stock Market Dashboard")
st.write("Explore and analyze stock market data interactively.")
st.markdown("---") # this is so amazing discovery



# we need to to the filters firts before the overview so that we can use the variables and operations within
#this
# 3. input
st.sidebar.header("Menu")
ticker = st.sidebar.selectbox("Select Stock", ["GOOGL", "AAPL", "MSFT", "AMZN", "TSLA"])

start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date",   value=pd.to_datetime("2025-01-01"))

ma_days = st.sidebar.slider("Moving Average", 10, 100, 50)



# to get the stock data this from yfinance
tickerData = yf.Ticker(ticker)
df = tickerData.history(start=start_date, end=end_date) #histpy fethc the price data betweeen chose dates adn return
#it to  the data frame well basically just a tabke with columns 



df["MA"] = df["Close"].rolling(ma_days).mean() # to smooth price over a number of days
df["Daily Return"] = df["Close"].pct_change() * 100 #to make it percentage since it gives decimals this from pandas
df["Year"] = df.index.year





# 2. DATASET OVERVIEW
#displaying dataset using metric from streamlit
# basically lito texts above the date year and chosen stock
st.subheader("Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Trading Days", len(df))
col2.metric("Date Range", f"{start_date.year} - {end_date.year}")
col3.metric("Stock", ticker)
st.markdown("---")




#to be able to displays plots and charts we need to first identify the mean median min max so that
#we have something to display within the chart
#I dont know how to do it so i used AI for this one with also understaning the code
st.subheader("Summary Statistics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Mean Close",   f"${df['Close'].mean():.2f}")
c2.metric("Median Close", f"${df['Close'].median():.2f}")
c3.metric("Max Close",    f"${df['Close'].max():.2f}")
c4.metric("Min Close",    f"${df['Close'].min():.2f}")

st.markdown("---") #to lang na ambag ko sa part na to




# 4. VISUALIZATIONS
st.subheader("Visualizations")


# we need to use the functions in matplotlib for this plots

# Line Chart 
st.write("### Chart 1: Closing Price & Moving Average")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df.index, df["Close"], label="Close Price", color="blue", linewidth=1.5)
ax1.plot(df.index, df["MA"],    label=f"{ma_days}-Day MA", color="orange", linestyle="--")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (USD)")
ax1.legend()
ax1.grid(alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)



# Chart 2: Bar Chart — Average Yearly Close
st.write("### Chart 2: Average Yearly Closing Price")
yearly_avg = df.groupby("Year")["Close"].mean()
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.bar(yearly_avg.index.astype(str), yearly_avg.values, color="steelblue")
ax2.set_xlabel("Year")
ax2.set_ylabel("Avg Close Price (USD)")
ax2.grid(alpha=0.3, axis="y")
plt.tight_layout()
st.pyplot(fig2)


# Chart 3: Histogram — Daily Returns
st.write("### Chart 3: Daily Return Distribution")
fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.hist(df["Daily Return"].dropna(), bins=50, color="purple", edgecolor="white")
ax3.axvline(df["Daily Return"].mean(),   color="red",    linestyle="--", label="Mean")
ax3.axvline(df["Daily Return"].median(), color="orange", linestyle="--", label="Median")
ax3.set_xlabel("Daily Return (%)")
ax3.set_ylabel("Frequency")
ax3.legend()
ax3.grid(alpha=0.3)
plt.tight_layout()
st.pyplot(fig3)

col_left, col_right = st.columns(2)


# Chart 4: Boxplot — Close Price by Year
with col_left:
    st.write("### Chart 4: Price Boxplot by Year")
    years    = sorted(df["Year"].unique())
    box_data = [df[df["Year"] == y]["Close"].values for y in years]
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    ax4.boxplot(box_data, labels=years)
    ax4.set_xlabel("Year")
    ax4.set_ylabel("Close Price (USD)")
    ax4.grid(alpha=0.3, axis="y")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig4)

# Chart 5: Pie Chart — Positive vs Negative Days
with col_right:
    st.write("### Chart 5: Positive vs Negative Days")
    pos = (df["Daily Return"] > 0).sum()
    neg = (df["Daily Return"] < 0).sum()
    fig5, ax5 = plt.subplots(figsize=(5, 4))
    ax5.pie([pos, neg],
            labels=["Positive Days", "Negative Days"],
            autopct="%1.1f%%",
            colors=["#4caf50", "#f44336"],
            startangle=140)
    plt.tight_layout()
    st.pyplot(fig5)


# Chart 6: Scatter Plot — Volume vs Close Price
st.write("### Chart 6: Scatter Plot — Volume vs Close Price")
fig6, ax6 = plt.subplots(figsize=(8, 4))
ax6.scatter(df["Volume"], df["Close"], alpha=0.3, color="teal", s=10)
ax6.set_xlabel("Volume")
ax6.set_ylabel("Close Price (USD)")
ax6.grid(alpha=0.3)
plt.tight_layout()
st.pyplot(fig6)

st.markdown("---")




# 5 Data table i have done this in my previous work its like data frame only (20) is to see the trading days with all columns
st.subheader("Data Table")
st.dataframe(df[["Open", "High", "Low", "Close", "Volume", "Daily Return"]].tail(20).round(2),
            use_container_width=True)

st.markdown("---")




# 6 insight I alsohave no idea how to use it so i just understand it at y best
st.subheader("Key Insights")
total_return = ((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100
pos_pct = pos / (pos + neg) * 100
best_day = df["Daily Return"].idxmax()
worst_day = df["Daily Return"].idxmin()

st.markdown(f"""
- **Total Return:** {ticker} gained **{total_return:.1f}%** over the selected period.
- **{pos_pct:.1f}%** of trading days were positive — stock trends **{"upward" if pos_pct > 50 else "downward"}**.
- **Best day** was {best_day.strftime('%B %d, %Y')} with **{df['Daily Return'].max():.2f}%** return.
- **Worst day** was {worst_day.strftime('%B %d, %Y')} with **{df['Daily Return'].min():.2f}%** return.
""")

st.markdown("---")
st.caption("Data Source: Yahoo Finance (https://pypi.org/project/yfinance/)")
