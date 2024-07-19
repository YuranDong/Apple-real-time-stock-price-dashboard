# Apple Stock Price Dashboard

## Overview

This project is a Streamlit-based web application that displays real-time stock data for Apple Inc. (AAPL). The application fetches stock data from Yahoo Finance, stores it in a MongoDB database, and provides a user-friendly interface to visualize the data in various time frames. The dashboard features real-time updates, candlestick charts using Plotly, and key stock metrics.

## Features

- **Real-time Data Updates:** The dashboard automatically refreshes every 60 seconds to display the latest stock data.
- **Time Period Selection:** Users can select different time periods (1 Hour, 1 Day, 1 Week, 1 Month) to view stock data.
- **Candlestick Charts:** Visualize stock price movements with interactive candlestick charts.
- **Stock Metrics Display:** Key metrics such as Open Price, Close Price, Volume, High Price, and Low Price are displayed.
- **Data Storage in MongoDB:** Stock data is stored in a MongoDB database for persistence and future analysis.

## Installation

### Prerequisites

- Python 3.6 or higher
- MongoDB server (local or cloud-based)

### Dependencies

Install the required Python libraries using pip:

```
pip install streamlit yfinance plotly pymongo pandas
```

### MongoDB Setup

Follow the installation guide for your operating system to install local MongoDB.

Follow the guide on mongodb official site to use the cloud-based MongoDB.


### Usage

## Clone the repository:

```
git clone https://github.com/YuranDong/Apple-real-time-stock-price-dashboard.git
cd apple-stock-dashboard
```

## Run the Streamlit application:

```
streamlit run app.py
```

## Open your web browser
navigate to http://localhost:8501

or visit https://apple-real-time-stock-price-dashboard-qgvjh9akjbetk6igosujn8.streamlit.app/ to see the dashboard right away.
