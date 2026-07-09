import pandas as pd

# Load the dataset
df = pd.read_csv("3101.csv")

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

# Display data types before conversion
print("Before Conversion:")
print(df.dtypes)

# Convert Price to float
df["Price"] = df["Price"].astype(float)

# Convert Quantity to int
df["Quantity"] = df["Quantity"].astype(int)

# Display data types after conversion
print("\nAfter Conversion:")
print(df.dtypes)
