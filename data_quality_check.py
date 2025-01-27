import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('weatherHistory.csv')

# Check for missing values
def check_missing_values(df):
    missing_values = df.isnull().sum()
    print(f"Missing values per column:\n{missing_values}")