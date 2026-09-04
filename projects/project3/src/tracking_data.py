import csv
import os

def save_tracking_data(
    filename,
    tracking_data
):
    if not tracking_data:
        print(
            f"No tracking data to save: "
            f"{filename}"
        )
        return

    directory = os.path.dirname(
        filename
    )

    if directory:
        os.makedirs(
            directory,
            exist_ok=True
        )

    fieldnames = list(
        tracking_data[0].keys()
    )

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(
            tracking_data
        )

    print(
        f"Tracking data saved to: "
        f"{filename}"
    )