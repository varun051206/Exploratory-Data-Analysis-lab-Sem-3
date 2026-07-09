import pandas as pd

# Load the dataset
df = pd.read_csv("Messy_Ecommerce.csv")

# Display missing values
print(df.isnull().sum())
