class CandleStick:
    def __init__(self, open_price, high_price, low_price, close_price, candle_type):
        self._open = open_price
        self._high = high_price
        self._low = low_price
        self._close = close_price
        if open_price==close_price:
            self._trend="Neutral"
        elif open_price<close_price:
            self._trend="Bullish"
        else:
            self._trend="Bearish"

        self._candle_type = candle_type

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        self._high = value

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        self._low = value

    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, value):
        self._close = value

    @property
    def trend(self):
        return self._trend

    @trend.setter
    def trend(self, value):
        self._trend = value

    @property
    def candle_type(self):
        return self._candle_type

    @candle_type.setter
    def candle_type(self, value):
        self._candle_type = value

    def __str__(self):
        return f"Candle: [Open={self._open}, High={self._high}, Low={self._low}, Close={self._close}, Trend={self._trend}, Type={self._candle_type}]"

# # Example usage:
# candle1 = CandleStick(10, 15, 8, 10, "Bullish", "Doji")
# print(candle1)
