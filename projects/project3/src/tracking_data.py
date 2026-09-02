import csv


def save_tracking_data(filename, tracking_data):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "frame",
                "time",
                "x_pixel",
                "y_pixel",
            ]
        )

        writer.writeheader()
        writer.writerows(tracking_data)