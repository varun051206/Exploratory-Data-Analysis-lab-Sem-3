# Import the Pandas library
import pandas as pd

# Load the dataset
df = pd.read_csv("Book1.csv")

# Display the first five records
print("First Five Records")
print(df.head())

# Display dataset information
print("\nDataset Information")
df.info()

# Display the dimensions of the dataset
print("\nDataset Shape")
print(df.shape)

# Display the statistical summary
print("\nStatistical Summary")
print(df.describe())
