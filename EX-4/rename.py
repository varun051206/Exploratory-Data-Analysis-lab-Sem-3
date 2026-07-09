import pandas as pd

# Load the dataset
df = pd.read_csv("3101.csv")

# Display original column names
print("Original Column Names:")
print(df.columns)

# Rename columns
df.rename(columns={
    'orderid': 'Order_ID',
    'cust': 'Customer_Name',
    'age': 'Age',
    'prod': 'Product',
    'qty': 'Quantity',
    'price': 'Price',
    'city': 'City'
}, inplace=True)

# Display updated column names
print("\nRenamed Column Names:")
print(df.columns)
