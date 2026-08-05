import pandas as pd

data = {
    "Math": [90, 85, 100, 70, 95]
}

df = pd.DataFrame(data)

print("Mean:", df["Math"].mean())
print("Sum:", df["Math"].sum())
print("Max:", df["Math"].max())
print("Min:", df["Math"].min())

print("\n=== Describe ===")
print(df.describe())