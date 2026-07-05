# Program 6: Display the Statistical Summary

# Import the Pandas library
import pandas as pd

# Load the dataset
df = pd.read_csv("EDA-Ex-1.csv")

# Display the statistical summary
print(df.describe())
