# create a 2-D list
import pandas as pd
data1 = [['AAA',25,'Pune'],
         ['BBB',30.'Mumbai'],
         ['CCC',35,'Nasik']+'complex']

#create a Dataframe from the list 
df = pd.Dataframe(data1, columns = ['Name','Age','City'])