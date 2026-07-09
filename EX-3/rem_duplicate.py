import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Remove duplicate records
df = df.drop_duplicates()

print(df)
