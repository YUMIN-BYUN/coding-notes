import matplotlib.pyplot as plt

def plot_fit(x, y, x_fit, y_fit, xlabel, ylabel, title):
    plt.plot(x_fit,y_fit, label = "Fitted curve")
    plt.scatter(x, y, label = "Raw Data")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

    