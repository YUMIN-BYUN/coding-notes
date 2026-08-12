class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self,stock):
        self.stocks.append(stock)

    def get_total_investment(self):
        total = 0
        for stock in self.stocks:
            total += stock.get_investment()
        return total
    
    def get_total_current_value(self):
        total = 0
        for stock in self.stocks:
            total += stock.get_current_value()
        return total

    def get_total_profit(self):
        return self.get_total_current_value() - self.get_total_investment()

    def get_total_return_rate(self):
        return (self.get_total_profit() / self.get_total_investment()) * 100

