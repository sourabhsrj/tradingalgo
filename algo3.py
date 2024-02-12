import yfinance as yf

# Define the symbol for Nifty 50 on Yahoo Finance
symbol = '^NSEI'

# Fetch real-time data (Note: This is delayed data, not true real-time)
nifty_data = yf.download(symbol, period='1d', interval='15m')

# Print the real-time candlestick data
print("Real-time Nifty Candlestick Data:")
# print(nifty_data.tail())
print("----------values---------")
# print(nifty_data.values)
print("----------values---------")
print("1 open ----2 high------ 3 low-----4 close")
data=nifty_data.values

print(type(data))
arraylist=data.tolist();
data=arraylist[len(arraylist)-1]
print(data)
# print(nifty_data.index)
