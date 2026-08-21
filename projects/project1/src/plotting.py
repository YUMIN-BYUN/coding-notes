import matplotlib.pyplot as plt
import numpy as np

def plot_raw_data(
    x,
    y,
    x_label,
    x_unit,
    y_label,
    y_unit,
    x_scale="linear",
    y_scale="linear"
):
    if x_scale not in ("linear", "log"):
        raise ValueError("x_scale must be 'linear' or 'log'.")

    if y_scale not in ("linear", "log"):
        raise ValueError("y_scale must be 'linear' or 'log'.")

    if x_scale == "log" and np.any(x <= 0):
        raise ValueError(
            "Log x-axis requires all x values to be positive."
        )

    if y_scale == "log" and np.any(y <= 0):
        raise ValueError(
            "Log y-axis requires all y values to be positive."
        )

    plt.figure()

    plt.scatter(x, y)

    plt.xscale(x_scale)
    plt.yscale(y_scale)

    if x_unit:
        plt.xlabel(f"{x_label} ({x_unit})")
    else:
        plt.xlabel(x_label)

    if y_unit:
        plt.ylabel(f"{y_label} ({y_unit})")
    else:
        plt.ylabel(y_label)

    plt.title("Raw Data")
    plt.grid(True)

    plt.show()

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