import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Display duplicate records
print(df[df.duplicated()])
