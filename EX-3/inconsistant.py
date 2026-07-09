import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Correct inconsistent values
df["Category"] = df["Category"].replace("clothing", "Clothing")

print(df)
