import requests
import json

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'BAJO0NHFEGVXJ9VH'
symbol = 'INDF'  # Nifty index symbol

# Alpha Vantage API endpoint for time series data
endpoint = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_INTRADAY'
interval = '1min'  # You can change this to '5min', '15min', '30min', or '60min' based on your needs

# Construct the API URL
url = f'{endpoint}?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}'

# Make the API request
response = requests.get(url)
data = response.json()

# Check if the request was successful
if 'Time Series (1min)' in data:
    # Extract the latest data
    latest_data = data['Time Series (1min)']
    latest_timestamp = max(latest_data.keys())
    latest_price = latest_data[latest_timestamp]['4. close']

    print(f"Latest Nifty data - Timestamp: {latest_timestamp}, Close Price: {latest_price}")
else:
    print(f"Failed to retrieve Nifty data. Check your API key and try again.")
