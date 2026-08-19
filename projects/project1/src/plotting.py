import matplotlib.pyplot as plt

def plot_fit(x, y, x_fit, y_fit, xlabel, xunit, ylabel, yunit, title):
    plt.figure()
    plt.plot(x_fit, y_fit, label="Fitted curve")
    plt.scatter(x, y, label="Raw Data")

    if xunit == "":
        plt.xlabel(xlabel) #dimensionless
    else:
        plt.xlabel(f"{xlabel} ({xunit})")

    if yunit == "":
        plt.ylabel(ylabel) #dimensionless
    else:
        plt.ylabel(f"{ylabel} ({yunit})")

    plt.title(title)
    plt.legend()
    plt.grid()


def plot_residuals(x, residuals, xlabel, xunit, yunit):
    plt.figure()
    plt.scatter(x, residuals)

    if xunit == "":
        plt.xlabel(xlabel) #dimensionless
    else:
        plt.xlabel(f"{xlabel} ({xunit})")

    if yunit == "":
        plt.ylabel("Residual") #dimensionless
    else:
        plt.ylabel(f"Residual ({yunit})")

    plt.title(f"Residual vs {xlabel}")
    plt.axhline(0)
    plt.grid()

def show_plots():
    plt.show()