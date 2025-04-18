# create a 2-D list
import pandas as pd
data1 = [['AAA',25,'Pune'],['BBB',30,'Mumbai'],['CCC',35,'Nasik']]

#create a Dataframe from the list 
df = pd.DataFrame(data1, columns = ['Name','Age','City'])
print(df)