from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

# Function to perform data quality checks (same as above)
def run_data_quality_checks():
    df = pd.read_csv('weatherHistory.csv')
    # Data quality checks here (same as the Python code above)