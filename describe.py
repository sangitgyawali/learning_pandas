#step-1 sample data frame

import pandas as pd

data ={
    "Name":['Ram', 'Shyam','Ghanashyam'],
    "Age":[10, 20, 30],
    "City":["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)
print("Descriptive Statistics")
print(df.describe())