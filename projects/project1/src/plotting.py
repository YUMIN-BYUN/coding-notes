import matplotlib.pyplot as plt
import numpy as np


def plot_raw_data(
    x,
    y,
    x_label,
    x_unit,
    y_label,
    y_unit,
    yerr=None,
    x_scale="linear",
    y_scale="linear"
):
    if x_scale not in ("linear", "log"):
        raise ValueError(
            "x_scale must be 'linear' or 'log'."
        )

    if y_scale not in ("linear", "log"):
        raise ValueError(
            "y_scale must be 'linear' or 'log'."
        )

    if x_scale == "log" and np.any(x <= 0):
        raise ValueError(
            "Log x-axis requires all x values to be positive."
        )

    if y_scale == "log" and np.any(y <= 0):
        raise ValueError(
            "Log y-axis requires all y values to be positive."
        )

    fig, ax = plt.subplots()

    if yerr is None:
        ax.scatter(
            x,
            y
        )
    else:
        ax.errorbar(
            x,
            y,
            yerr=yerr,
            fmt="o",
            capsize=3
        )

    ax.set_xscale(x_scale)
    ax.set_yscale(y_scale)

    if x_unit:
        ax.set_xlabel(
            f"{x_label} ({x_unit})"
        )
    else:
        ax.set_xlabel(
            x_label
        )

    if y_unit:
        ax.set_ylabel(
            f"{y_label} ({y_unit})"
        )
    else:
        ax.set_ylabel(
            y_label
        )

    ax.set_title(
        "Raw Data"
    )

    ax.grid(True)

    return fig


def plot_fit(
    x,
    y,
    x_fit,
    y_fit,
    xlabel,
    xunit,
    ylabel,
    yunit,
    title,
    yerr=None,
    x_scale="linear",
    y_scale="linear"
):
    if x_scale not in ("linear", "log"):
        raise ValueError(
            "x_scale must be 'linear' or 'log'."
        )

    if y_scale not in ("linear", "log"):
        raise ValueError(
            "y_scale must be 'linear' or 'log'."
        )

    if x_scale == "log" and np.any(x <= 0):
        raise ValueError(
            "Log x-axis requires all x values to be positive."
        )

    if y_scale == "log" and (
        np.any(y <= 0)
        or np.any(y_fit <= 0)
    ):
        raise ValueError(
            "Log y-axis requires all y values "
            "and fitted values to be positive."
        )

    fig, ax = plt.subplots()

    ax.plot(
        x_fit,
        y_fit,
        label="Fitted Curve"
    )

    if yerr is None:
        ax.scatter(
            x,
            y,
            label="Raw Data"
        )
    else:
        ax.errorbar(
            x,
            y,
            yerr=yerr,
            fmt="o",
            capsize=3,
            label="Raw Data"
        )

    ax.set_xscale(x_scale)
    ax.set_yscale(y_scale)

    if xunit:
        ax.set_xlabel(
            f"{xlabel} ({xunit})"
        )
    else:
        ax.set_xlabel(
            xlabel
        )

    if yunit:
        ax.set_ylabel(
            f"{ylabel} ({yunit})"
        )
    else:
        ax.set_ylabel(
            ylabel
        )

    ax.set_title(
        title
    )

    ax.legend()
    ax.grid(True)

    return fig


def plot_residuals(
    x,
    residuals,
    xlabel,
    xunit,
    yunit,
    x_scale="linear"
):
    if x_scale not in ("linear", "log"):
        raise ValueError(
            "x_scale must be 'linear' or 'log'."
        )

    if x_scale == "log" and np.any(x <= 0):
        raise ValueError(
            "Log x-axis requires all x values to be positive."
        )

    fig, ax = plt.subplots()

    ax.scatter(
        x,
        residuals
    )

    ax.set_xscale(
        x_scale
    )

    if xunit:
        ax.set_xlabel(
            f"{xlabel} ({xunit})"
        )
    else:
        ax.set_xlabel(
            xlabel
        )

    if yunit:
        ax.set_ylabel(
            f"Residual ({yunit})"
        )
    else:
        ax.set_ylabel(
            "Residual"
        )

    ax.set_title(
        f"Residual vs {xlabel}"
    )

    ax.axhline(0)
    ax.grid(True)

    return fig


def show_plots():
    plt.show()