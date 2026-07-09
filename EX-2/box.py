# Program 4: Box Plot

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data Set.csv")

# Remove extra spaces
df.columns = df.columns.str.strip()

# Create Box Plot
plt.figure(figsize=(6,5))
plt.boxplot(df["Final MRP Old"])

plt.title("Box Plot of Final MRP Old")
plt.ylabel("Final MRP Old")

plt.grid(True)

plt.show()
