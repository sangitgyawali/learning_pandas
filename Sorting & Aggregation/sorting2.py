import pandas as pd

data ={
    "Name":['Arun', 'Varun','Karun'],
    "Age":[28, 34, 22],
    "Salary":[10000, 20000, 30000]
}

df= pd.DataFrame(data)
df.sort_values(by=["Age", "Salary"], ascending=False, inplace=True)
print('Sorted Age by Descending')
print(df)