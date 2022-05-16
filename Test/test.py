import unittest
import app.Exchane as Exchange
from app.Share import Stock
from app.Trade import Trade
from random import choice
from data.sample_data import data


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        """Application end-to-end test"""
        self.Market = Exchange.Exchange()
        pass

    def test_divident_calc(self):
        """Test the dvidend yield the dividend yield."""

        s = Stock()

        # common
        setattr(s, "Stock", "POP")
        setattr(s, "Type", "Common")
        setattr(s, "Last_Div", 8)

        dy = s.dividend_yield(250)
        self.assertEqual(8 / 250, dy)

        # preferred
        setattr(s, "Stock", "GIN")
        setattr(s, "Type", "Preferred")
        setattr(s, "Fixed_Div", 2)
        setattr(s, "Par", 100)

        dy = s.dividend_yield(402)
        self.assertEqual(2 / 100 * 100 / 402, dy)

    def test_pe_ratio_calc(self):
        """Test PE Ratio"""

        s = Stock()
        setattr(s, "Last_Div", 23)

        for iter in range(100):
            price = choice(range(1, 1000))
            pe = s.pe_ratio(price)
            self.assertEqual(price / getattr(s, "Last_Div", 1),
                             s.pe_ratio(price))

    def test_trade_recoding(self):
        """Testing the Trade recordingb function , add_stock"""
        s = Stock()
        setattr(s, "Stock", "GIN")
        setattr(s, "Type", "Preferred")
        setattr(s, "Fixed_Div", 2)
        setattr(s, "Par", 100)

        self.Market.add_stock(s)

        t =Trade()
        setattr(t, "Stock", "GIN")
        setattr(t, "Action(Buy/Sell)", 'Buy')
        setattr(t, "Qty", 1000)
        setattr(t, "Price", 114)
        self.Market.add_trade(t)  # adds Timestamp

        self.assertTrue(len(self.Market.trades) > 0)

        # verify timestamp added ok
        self.assertIsNotNone(self.Market.trades[0].Timestamp)




if __name__ == "__main__":
    unittest.main()
