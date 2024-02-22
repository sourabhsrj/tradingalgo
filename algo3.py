from candlestickanalysis import CandleStick
import yfinance as yf

from candlestickanalysis.BearishCandles.DragonflyDoji import DragonflyDoji

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
data = nifty_data.values

# print(type(data))
arraylist = data.tolist();
data = arraylist[len(arraylist) - 1]
# print(data)


print(nifty_data.index)
d1 = data[0]
d2 = data[1]
d3 = data[2]
d4 = data[3]

list=[]

for d in arraylist:
    list.append(CandleStick.CandleStick(d[0],d[1],d[2],d[3],"neutral"))

for obj in list:
    print(obj)
