TRADE_FIELDS_LIST = ["Timestamp", "Stock", "Qty", "Action(Buy/Sell)", "Price"]

class Trade:
    """
    A Trade represents a purchase or sale of a quantity of stock
    """
    def __init__(self):
        """Create a new buy or sell trade instruction."""
        for f in TRADE_FIELDS_LIST:
            setattr(self, f, None)

    def validate(self):
        """Validate a Trade entry"""
        for f in TRADE_FIELDS_LIST:
            if getattr(self,f,None) is None:
                return False

        return True