import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Fill missing numerical values with mean
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
df["Stock"] = df["Stock"].fillna(df["Stock"].mean())

print(df)
