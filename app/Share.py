
from datetime import datetime as dt, timedelta

STOCK_FIELDS_LIST = ["Stock","Type","Last_Div","Fixed_Div","Par"]
TRADE_FIELDS_LIST = ["Time", "Stock", "Qty", "Action(Buy/Sell)", "Price"]

class Stock:

    def __init__(self):
        for f in STOCK_FIELDS_LIST:
            setattr(self, f, None)

    def div_yield(self, price):
        """dividend_yield`"""
        return self.dividend_yield(price)

    def dividend_yield(self, price):
        """Given a price, return the Dividend Yield of this stock."""
        if self.Type == "Common":
            return getattr(self, "Last_Div")/price
        else: # preferred
            div=getattr(self, "Fixed_Div")
            par =getattr(self, "Par")
            return (div/100) * (par/price)

    def pe_ratio(self, price):
        """Given a price, return pe ratio."""
        div=getattr(self, "Last_Div")
        return price / div
