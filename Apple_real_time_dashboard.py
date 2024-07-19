# Import required libraries and functions
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta
import time
import pandas as pd
from pymongo import MongoClient

# Set the refresh interval (in seconds)
refresh_interval = 60

# Define the available time periods and corresponding yfinance intervals
time_periods = {
    '1 Hour': ('5m', '1d'),
    '1 Day': ('1h', '1d'),
    '1 Week': ('1h', '5d'),
    '1 Month': ('1h', '1mo')
}

# MongoDB connection setup, using local mongodb and designed portal
# comment because time error
# mongo = 'mongodb+srv://dyr_globalai:3H4xLhE9UfgfTrOk@cluster0.cvguqnb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# client = MongoClient(mongo)
# db = client['stock_data_db']
# collection = db['apple_stock']


# Function to get stock data based on the selected time period
def get_stock_data(company, period, interval):
    stock_data = yf.Ticker(company)
    stock_info = stock_data.history(period=period, interval=interval)
    stock_info.reset_index(inplace=True)
    stock_info['Datetime'] = stock_info['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return stock_info

# Function to store data in MongoDB
def store_data_in_mongodb(data, collection):
    data_dict = data.to_dict("records")
    collection.insert_many(data_dict)

# Function to get data from MongoDB
def get_data_from_mongodb(collection):
    data = list(collection.find())
    return pd.DataFrame(data)

# Get data for Apple's stock
company = "AAPL"

# Dashboard layout
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Apple Stock Price Dashboard</h1>", unsafe_allow_html=True)
selected_period = st.selectbox("Select Time Period", list(time_periods.keys()), key='time_period', index=2)
interval, period = time_periods[selected_period]
stock_info = get_stock_data(company, period, interval)

# Store the data in MongoDB
# store_data_in_mongodb(stock_info, collection)

# Extract the most recent data based on the selected period
recent_data = stock_info.iloc[-1]

# Extract the relevant data
open_price = recent_data['Open']
close_price = recent_data['Close']
volume = recent_data['Volume']
high_price = recent_data['High']
low_price = recent_data['Low']

# Create columns for each metric
col1, col2, col3, col4, col5 = st.columns(5)

# Display the metrics
col1.metric("Open Price", f"${open_price:.2f}")
col2.metric("Close Price", f"${close_price:.2f}")
col3.metric("Volume", f"{volume:,}")
col4.metric("High Price", f"${high_price:.2f}")
col5.metric("Low Price", f"${low_price:.2f}")

# Center the data table
st.markdown("<h2 style='text-align: center;'>Recent data for Apple's stock:</h2>", unsafe_allow_html=True)

# Use columns to center the dataframe
col6, col7, col8 = st.columns([2, 3, 1])
with col7:
    st.dataframe(stock_info[['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']], height = 200)

# Plotting the candlestick chart using Plotly
fig = go.Figure(data=[go.Candlestick(x = stock_info['Datetime'],
                                     open = stock_info['Open'],
                                     high = stock_info['High'],
                                     low = stock_info['Low'],
                                     close = stock_info['Close'])])

# Update layout to connect gaps (like weekends) in the chart and clean date labels
fig.update_layout(
    title = f'Apple Stock Price ({selected_period})',
    xaxis_title = 'Date',
    yaxis_title = 'Price (USD)',
    xaxis_rangeslider_visible = False,
    xaxis = dict(
        type = 'category',
        tickmode = 'auto',
        nticks = 10
    )
)
st.plotly_chart(fig, use_container_width=True)

# Automatically refresh the app every refresh_interval seconds
time.sleep(refresh_interval)
st.experimental_rerun()
