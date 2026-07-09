# Program 2: Pie Chart

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data Set.csv")

# Count products in each category
category_count = df['Category'].value_counts()

# Create Pie Chart
plt.figure(figsize=(7,7))
category_count.plot(kind='pie', autopct='%1.1f%%')

plt.title("Product Category Distribution")
plt.ylabel("")

plt.show()
