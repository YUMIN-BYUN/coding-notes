import matplotlib.pyplot as plt

def plot_returns(df):
    x = df["ticker"]
    y = df["return_rate"]
    plt.bar(x,y)
    plt.xlabel("Ticker")
    plt.ylabel("Return Rate(%)")
    plt.title("Return Rate(%) by Ticker")
    plt.axhline(0)

    plt.savefig("output/return_rates.png")
    
    plt.show()