import pandas as pd

def create_dataframe(portfolio):
    data = []
    for stock in portfolio.stocks:
        data.append({
            "ticker": stock.ticker,
            "shares": stock.shares,
            "investment": stock.get_investment(),
            "current_value": stock.get_current_value(),
            "profit": stock.get_profit(),
            "return_rate": stock.get_return_rate()
        })

    df = pd.DataFrame(data)
    return df

def analyze_portfolio(df):
    sorted_df = df.sort_values("return_rate", ascending=False)
    best_stock = sorted_df.iloc[0]
    worst_stock = sorted_df.iloc[-1]
    print("=== Portfolio Analysis ===")
    print(f"Best Stock: {best_stock['ticker']} ({best_stock['return_rate']:.2f}%)")
    print(f"Worst Stock: {worst_stock['ticker']} ({worst_stock['return_rate']:.2f}%)")