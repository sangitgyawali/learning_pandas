# df["Column Name"].mean()
# df["Column Name"].sum()
# df["Column Name"].min()
# df["Column Name"].max()

import pandas as pd

data ={
    "Name":['Arun', 'Varun','Karun'],
    "Age":[28, 34, 22],
    "Salary":[10000, 20000, 30000]
}

df= pd.DataFrame(data)

print(df)

avg_salary = df['Salary'].mean()
print(avg_salary)