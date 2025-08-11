import pandas as pd

data ={
    "Name":['Ram', 'Shyam','Ghanashyam'],
    "Age":[10, 20, 30],
    "City":["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

#display the dataframe
print("Sample Dataframe")
print(df)
print("Names (Single column return series)")
name = df["Name"]
print(name)