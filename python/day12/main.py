import pandas as pd
from stock import Stock
from portfolio import Portfolio
from analysis import create_dataframe, analyze_portfolio
from visualization import plot_returns

df = pd.read_csv("data/portfolio.csv")

portfolio = Portfolio()

for index, row in df.iterrows():
    stock = Stock(
        row["ticker"],
        row["shares"],
        row["buy_price"],
        row["current_price"]
    )
    portfolio.add_stock(stock)

analysis_df = create_dataframe(portfolio)
print(analysis_df)
analyze_portfolio(analysis_df)
plot_returns(analysis_df)

analysis_df.to_csv("output/portfolio_analysis.csv", index=False)