# Program 3: Display the Last Five Records

# Import the Pandas library
import pandas as pd

# Load the dataset
df = pd.read_csv("EDA-Ex-1.csv")

# Display the last five records
print(df.tail())
