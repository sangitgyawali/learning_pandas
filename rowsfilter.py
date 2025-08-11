import pandas as pd

data ={
    "Name":['Ram', 'Shyam','Ghanashyam'],
    "Age":[10, 20, 30],
    "City":["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

age = df[df['Age'] > 20]
print("Employee with Age > 20")
print(age)