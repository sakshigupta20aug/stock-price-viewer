import yfinance as yf
import streamlit as st
import datetime

st.title("📈 Simple Stock Price Viewer")

st.write("Select a company and date range to view its historical stock data (Closing Price & Volume).")

# 📌 Dictionary of popular tickers and their company names
ticker_dict = {
    "GOOGL": "Alphabet (Google)",
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corp",
    "AMZN": "Amazon.com Inc.",
    "TSLA": "Tesla Inc.",
    "META": "Meta Platforms (Facebook)",
    "NFLX": "Netflix Inc.",
    "NVDA": "NVIDIA Corp",
    "IBM": "International Business Machines",
    "INTC": "Intel Corp",
    "BA": "Boeing Co",
    "JPM": "JPMorgan Chase",
    "WMT": "Walmart Inc.",
    "DIS": "Walt Disney Co",
    "T": "AT&T Inc."
}

# 📋 Dropdown to select ticker
selected_ticker = st.selectbox(
    "Select a Company",
    options=list(ticker_dict.keys()),
    format_func=lambda x: ticker_dict[x]
)

# 📆 Let user pick date range
st.write("Select date range:")
start_date = st.date_input("Start Date", datetime.date(2015, 1, 1))
end_date = st.date_input("End Date", datetime.date.today())

# 🚨 Validate date input
if start_date >= end_date:
    st.error("End date must be after start date.")
else:
    # ⏳ Load stock data
    ticker_data = yf.Ticker(selected_ticker)
    ticker_df = ticker_data.history(start=start_date, end=end_date)

    company_name = ticker_dict[selected_ticker]

    if ticker_df.empty:
        st.warning("No data available for the selected date range.")
    else:
        # 📈 Show charts
        st.subheader(f"{company_name} ({selected_ticker}) - Closing Price")
        st.line_chart(ticker_df.Close)

        st.subheader(f"{company_name} ({selected_ticker}) - Volume")
        st.line_chart(ticker_df.Volume)
