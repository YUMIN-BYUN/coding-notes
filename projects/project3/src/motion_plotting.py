import matplotlib.pyplot as plt


def plot_motion(tracking_data):
    if not tracking_data:
        raise ValueError(
            "No tracking data available for plotting."
        )

    time = [
        point["time"]
        for point in tracking_data
    ]

    x = [
        point["x"]
        for point in tracking_data
    ]

    y = [
        point["y"]
        for point in tracking_data
    ]

    # x(t)
    plt.figure()

    plt.plot(
        time,
        x,
        marker="o"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("x (m)")
    plt.title("Horizontal Motion: x(t)")
    plt.grid()

    # y(t)
    plt.figure()

    plt.plot(
        time,
        y,
        marker="o"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("y (m)")
    plt.title("Vertical Motion: y(t)")
    plt.grid()

    # y(x)
    plt.figure()

    plt.plot(
        x,
        y,
        marker="o"
    )

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectory: y(x)")
    plt.grid()

    plt.show()