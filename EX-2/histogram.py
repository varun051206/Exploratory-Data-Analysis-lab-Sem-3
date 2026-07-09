# Program 3: Histogram

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data Set.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Create Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Final MRP Old"], bins=10, edgecolor="black")

plt.title("Distribution of Final MRP Old")
plt.xlabel("Final MRP Old")
plt.ylabel("Frequency")

plt.grid(True)

plt.show()
