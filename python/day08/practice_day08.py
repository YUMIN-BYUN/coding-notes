import pandas as pd

data = {
    "Name" : ["Kim", "Lee", "Park", "Choi"],
    "Math" : [90, 85, 100, 95],
    "English" : [88, 91, 95, 87]
}

df = pd.DataFrame(data)

df["Physics"] = [92, 84, 98, 90]

print("==== Student Data ====")
print(df)

print()
print(df["Math"])

print()
print(df.iloc[1])

print()
df = df.drop(columns=["English"])
print(df)

df.to_csv("student.csv", index = False)
loaded = pd.read_csv("student.csv")

print()
print("Average : ",loaded["Math"].mean())
print("Maximum : ",loaded["Math"].max())
print("Minimum : ",loaded["Math"].min())

print()
print(loaded.describe())