import pandas as pd

data = {
    "Name": ["Kim", "Lee", "Park"],
    "Math": [90, 85, 100]
}

df = pd.DataFrame(data)

print("=== Original ===")
print(df)
print()

df["Physics"] = [95, 80, 90]

print("=== After Adding Physics ===")
print(df)
print()

df = df.drop(columns=["Math"])

print("=== After Deleting Math ===")
print(df)