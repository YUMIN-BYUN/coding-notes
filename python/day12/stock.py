class Stock:
    def __init__(self,ticker,shares,buy_price,current_price):
        self.ticker = ticker
        self.shares = shares
        self.buy_price = buy_price
        self.current_price = current_price

    def get_investment(self):
        return self.shares * self.buy_price

    def get_current_value(self):
        return self.shares * self.current_price

    def get_profit(self):
        return self.get_current_value() - self.get_investment()

    def get_return_rate(self):
        return (self.get_profit() / self.get_investment()) * 100
