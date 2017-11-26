import pandas as pd

class Trading:


    def __init__(self):
        self.CI=pd.DataFrame(columns=["ticker","position","quantity","Open","Current_Close","OpenDate","CloseDate",
                                       ])


        self.PnL=pd.DataFrame(columns=[])

        pass

    def stock_trade_cityindex(self, ticker, price, quantity, direction,commission, currency):
        """
        ticker (str) for standard chartered currency should contain only the target currency

        quantity (int) number of stocks or currency traded
        direction (int) long=1, short=-1
        margin  (float) percentage of margin required

        :param ticker: (str) for standard chartered currency should contain only the target currency
        :param price:  (float) trade price
        :param quantity: (int) number of stocks or currency traded
        :param direction: (int) long=1, short=-1
        :param commission: (float)
        :param currency: (str)  currency of stock
        :param rate: (float)    currency rate

        :return: None
        """


        dasfdsa





x=MyClass()

x.data.append(10)

print(x.data)