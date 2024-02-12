import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from mplfinance.original_flavor import candlestick_ohlc
from nsetools import Nse
from datetime import datetime


def fetch_nifty_candlestick_data(symbol, interval='5minute', num_candles=50):
    nse = Nse()
    stock_data = nse.get_stock_codes()

    if symbol not in stock_data:
        print(f"Symbol {symbol} not found.")
        return None

    historical_data = nse.get_historical(symbol, start=datetime.now().strftime('%Y-%m-%d'), interval=5)

    if not historical_data:
        print(f"Unable to fetch data for {symbol}.")
        return None

    ohlc_data = []
    for candle in historical_data[-num_candles:]:
        timestamp = datetime.strptime(candle['timestamp'], '%Y-%m-%d %H:%M:%S')
        ohlc_data.append((timestamp, candle['open'], candle['high'], candle['low'], candle['close']))

    return ohlc_data


def plot_candlestick_chart(symbol, ohlc_data):
    fig, ax = plt.subplots()

    mondays = WeekdayLocator(MONDAY)  # major ticks on the mondays
    alldays = DayLocator()  # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')  # e.g., 12

    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)

    candlestick_ohlc(ax, ohlc_data, width=0.6, colorup='g', colordown='r')

    ax.xaxis_date()
    ax.autoscale_view()

    plt.title(f'Candlestick Chart for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()


if __name__ == "__main__":
    nifty_symbol = 'NIFTY'
    candlestick_data = fetch_nifty_candlestick_data(nifty_symbol)

    if candlestick_data:
        plot_candlestick_chart(nifty_symbol, candlestick_data)
