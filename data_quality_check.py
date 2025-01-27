import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('weatherHistory.csv')

# Check for missing values
def check_missing_values(df):
    missing_values = df.isnull().sum()
    print(f"Missing values per column:\n{missing_values}")

# Check for duplicates
def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")

# Check for logical inconsistencies (e.g., temperature in extreme ranges)
def check_inconsistencies(df):
    inconsistent_temps = df[(df['Temperature (C)'] < -50) | (df['Temperature (C)'] > 50)]
    print(f"Inconsistent temperature values:\n{inconsistent_temps}")

# Check for outliers (e.g., wind speed above 200 km/h)
def check_outliers(df):
    outliers = df[df['Wind Speed (km/h)'] > 200]
    print(f"Outliers in wind speed:\n{outliers}")