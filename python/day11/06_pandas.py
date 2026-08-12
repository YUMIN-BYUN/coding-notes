import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Physics": [88, 76, 95, 82, 91],
    "Math": [92, 85, 90, 78, 94]
}

#1
df = pd.DataFrame(data)
print(df)
print()

#2
print(df["Physics"])
print(df["Name"])
print()

#3
print(df.loc[2])
print(df.loc[1:3,["Name","Physics"]])
print()

#4
print(df.iloc[0])
print(df.iloc[-1])
print()

#5
df["Average"] = (df["Physics"] + df["Math"])/2
print(df)
print()

#6
print(f"Average of Physics: {df['Physics'].mean()}")
print(f"Average of Math: {df['Math'].mean()}")
print(f"Maximum of Physics: {df['Physics'].max()}")
print(f"Minimum of Math: {df['Math'].min()}")
print()

#7
print(df.describe())