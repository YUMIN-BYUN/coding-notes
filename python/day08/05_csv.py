import pandas as pd

data = {
    "Name": ["Kim", "Lee", "Park"],
    "Math": [90, 85, 100],
    "English": [88, 91, 95]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

loaded = pd.read_csv("students.csv")

print("=== Loaded CSV ===")
print(loaded)

print()
print(type(loaded))