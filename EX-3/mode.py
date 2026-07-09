import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Fill missing categorical values with mode
df["Category"] = df["Category"].fillna(df["Category"].mode()[0])

print(df)
