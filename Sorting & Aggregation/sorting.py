# Sorting data
# SORTING DATA 1 COLUMN using sort_values()
# df.sort_values(by="Column Name", True/False, inplace = True)

import pandas as pd

data ={
    "Name":['Arun', 'Varun','Karun'],
    "Age":[28, 34, 22],
    "Salary":[10000, 20000, 30000]
}

df= pd.DataFrame(data)
df.sort_values(by="Age", ascending=False, inplace=True)
print('Sorted Age by Descending')
print(df)