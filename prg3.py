# Create series from python dictionary
import pandas as pd
# create a dictionary
grades = {
    "Semester1": 4.45,
    "Semester2": 4.35,
    "Semester3": 4.40,
}
# create a series from the dictionary
seriesd = pd.Series(grades)
# display the series
print(seriesd)
# select specific dictionary items using index
seriesd = pd.Series(grades,index = ["Semester1", "Semester2"])
print(seriesd)