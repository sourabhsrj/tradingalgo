class DragonflyDoji:
    name = "Dragonfly Doji"
    candle_type="Bearish"
    candle_info="Bearish"
    dragonflydoji=False

    @classmethod
    def is_dragonfly_doji(open_price, high_price, low_price, close_price):
        if open_price == high_price and close_price == high_price and low_price < open_price:
            dragonflydoji=True
        return True

