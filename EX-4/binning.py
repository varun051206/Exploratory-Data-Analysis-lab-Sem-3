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

# Equal-Width Binning
df["Age_EqualWidth"] = pd.cut(
    df["Age"],
    bins=4,
    labels=["Young", "Adult", "Middle Age", "Senior"]
)

# Equal-Frequency Binning
df["Age_EqualFrequency"] = pd.qcut(
    df["Age"],
    q=4,
    labels=["Young", "Adult", "Middle Age", "Senior"]
)

# Display result
print(df[["Age", "Age_EqualWidth", "Age_EqualFrequency"]])
