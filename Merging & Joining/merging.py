import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})

df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 350]
})

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
print("Left join")
print(df_merged)