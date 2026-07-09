import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Perform data cleaning
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
df["Stock"] = df["Stock"].fillna(df["Stock"].mean())
df["Category"] = df["Category"].replace("clothing", "Clothing")
df = df.drop_duplicates()

# Verify cleaned dataset
print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nCleaned Dataset:")
print(df)
