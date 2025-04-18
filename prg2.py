import pandas as pd
li = [1,3,5]
# creatin labels doe the list
series1 = pd.Series(li, index = ["x", "y", "z"])
print(series1)
print(series1["y"])