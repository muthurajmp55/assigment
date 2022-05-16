
from datetime import datetime as dt, timedelta

class Exchange:

    def __init__(self):
        """Create the stock market with a placeholder list for the Stocks & Trades."""
        self.stocks = []
        self.trades = []

    def add_stock(self, stock):
        """Add a new Stock to the exchange."""
        symbol = getattr(stock, "Stock", None)

        if not bool(symbol):
            raise RuntimeError("A new Stock must have a unique Stock to be added to the exchange.")

        if bool(len(list(filter(lambda x: getattr(x, "Stock", "") == symbol, self.stocks)))):
            raise RuntimeError("A stock with symbol {} already exists in the exchange.".format(symbol))

        self.stocks.append(stock)
        return True

    def get_stock(self, symbol):
        """Retrieve a Stock object from the exchange."""
        match = list(filter(lambda x: getattr(x, "Stock") == symbol, self.stocks))
        if match:
            return match[0]
        else:
            return None

    def add_trade(self, trade):
        """Record a new Trade on the exchange."""

        if not trade.Timestamp:
            trade.Timestamp = dt.utcnow()

        if not trade.validate():
            raise RuntimeError("Cannot add an incomplete Trade to the exchange.")

        # a trade must be for a stock on our exchange
        symb = getattr(trade, "Stock")
        if not self.get_stock(symb):
            raise RuntimeError("Cannot add a Trade for unknown Stock Symbol {}".format(symb))

        self.trades.append(trade)
        return True

    def volume_weighted_stock_price(self, symbol=None):
        """Given a stock symbol, return the volume-weighted price for that stock in the past 5 minutes."""
        stock = self.get_stock(symbol)

        if not stock:
            raise RuntimeError("Cannot calculate Volume Weighted Stock Price for non-existent stock {}". \
                               format(symbol))

        if symbol:
            relevant_trades = list(filter(lambda x: getattr(x, "Stock Symbol") == symbol \
                                                    and dt.utcnow() - x.Timestamp <= timedelta(minutes=5),
                                          self.trades))
        else:
            relevant_trades = self.trades

        try:
            return Exchange.volume_weighted_stock_price(relevant_trades)
        except TypeError:
            return 0

    @staticmethod
    def volume_weighted_stock_price(trades):
        if len(trades):
            return float('{p:.2f}'.format(p=sum(map(lambda x: x.Price * x.Qty, trades))/ sum(map(lambda x: x.Qty, trades))))
        else:
            return None

    @staticmethod
    def geo_mean(stks_list):
        pro = stks_list[0]

        if len(stks_list) > 1:
            for s in stks_list[1:]:
                pro = pro * s

        return pro ** (1.0 / len(stks_list))