# Program 5: Scatter Plot

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data Set.csv")

# Remove extra spaces
df.columns = df.columns.str.strip()

# Create Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["TP 1"], df["Final MRP Old"])

plt.title("TP 1 vs Final MRP Old")
plt.xlabel("TP 1")
plt.ylabel("Final MRP Old")

plt.grid(True)

plt.show()
