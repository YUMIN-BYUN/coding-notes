import pandas as pd
import numpy as np

def load_experimental_data(file_path):
    df = pd.read_csv(file_path)

    print(f"{list(df.columns)}\n")

    while True:
        x_column = input("Select x column: ")

        if x_column in df.columns:
            try:
                x = pd.to_numeric(df[x_column], errors="raise").to_numpy()
                if np.isfinite(x).all():
                    break
                else:
                    print("Selected x column contains NaN or infinite values")
                    continue
            except ValueError:
                print("Selected x column must contain numeric data")
                continue

        print("Invalid column. Try again.")

    while True:
        y_column = input("Select y column: ")

        if y_column in df.columns:
            try:
                y = pd.to_numeric(df[y_column], errors="raise").to_numpy()
                if np.isfinite(y).all():
                    break
                else:
                    print("Selected y column contains NaN or infinite values")
                    continue 
            except ValueError:
                print("Selected y column must contain numeric data")
                continue

        print("Invalid column. Try again.")

    while True:
        yerr_column = input(
                "Select y uncertainty column (leave blank if none): "
            )

        if yerr_column == "":
            yerr = None   
            break

        if yerr_column in df.columns:
            try:
                yerr = pd.to_numeric(df[yerr_column], errors="raise").to_numpy()
                if not np.isfinite(yerr).all():
                    print("Selected y uncertainty column contains NaN or infinite values")
                    continue
                if not (yerr > 0).all():
                    print("Y uncertainty must be positive.")
                    continue

                break

            except ValueError:
                print("Selected y uncertainty column must contain numeric data")
                continue
            
        print("Invalid column. Try again.")
    
    return x, y, yerr



