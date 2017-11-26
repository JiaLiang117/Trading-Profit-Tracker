import pandas as pd


class Trading:
    def __init__(self):
        # CI Journel Entries

        self.CI = pd.DataFrame(
            columns=["id", "ticker", "position", "quantity", "Open", "Current_Close", "OpenDate", "CloseDate",
                     "margin", "commissions", "currency", "rate", "cc_pnl", "sgd_pnl", "total return"])

        # income statement
        self.PnL = pd.DataFrame(columns=["ticker", "position", "quantity", "pnl"])


    def stock_trade_cityindex(self, ticker, price, quantity, direction, commission, currency):
        """
        ticker (str) for standard chartered currency should contain only the target currency

        quantity (int) number of stocks or currency traded
        direction (int) long=1, short=-1
        margin  (float) percentage of margin required

        :param ticker: (str) for standard chartered currency should contain only the target currency
        :param price:  (float) trade price
        :param quantity: (int) number of stocks or currency traded
        :param direction: (int) long=1, short=-1
        :param margin: (float) percentage of margin required
        :param commission: (float) total commission cost
        :param currency: (str)  currency of stock
        :param rate: (float)    currency rate
        :param open: (int) 1 for open, 0 for close

        :return: None
        """






x = MyClass()

x.data.append(10)

print(x.data)
