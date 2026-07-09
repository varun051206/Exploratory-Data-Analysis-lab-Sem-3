# Program 1: Bar Chart

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data Set.csv")

# Count products in each category
category_count = df['Category'].value_counts()

# Create Bar Chart
plt.figure(figsize=(8,5))
category_count.plot(kind='bar')

plt.title("Product Count by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")

plt.show()
