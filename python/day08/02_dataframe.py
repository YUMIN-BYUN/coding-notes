import pandas as pd

data = {
    "Name": ["Kim", "Lee", "Park"],
    "Math": [90, 85, 100],
    "English": [88, 91, 95]
}

df = pd.DataFrame(data)

print(df)