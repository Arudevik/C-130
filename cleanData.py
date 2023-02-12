import pandas as pd

data = pd.read_csv("Pro-130/previousData.csv")

del data["Star_name"]

data = data.dropna()

data.to_csv("Pro-130/newdata.csv")




