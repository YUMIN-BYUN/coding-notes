import pandas as pd

data = {
    "Name": ["Kim", "Lee", "Park"],
    "Math": [90, 85, 100],
    "English": [88, 91, 95]
}

df = pd.DataFrame(data)

print("=== Math Column ===")
print(df["Math"])
print()

print("=== Math & English ===")
print(df[["Math", "English"]])
print()

print("=== First Row ===")
print(df.iloc[0])
print()

print("=== Value (Row 1, Column 2) ===")
print(df.iloc[1, 2])