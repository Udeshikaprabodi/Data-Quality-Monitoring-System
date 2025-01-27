from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

# Function to perform data quality checks (same as above)
def run_data_quality_checks():
    df = pd.read_csv('weatherHistory.csv')
    # Data quality checks here (same as the Python code above)

# Define the DAG
dag = DAG(
    'data_quality_check',
    description='Data quality check DAG',
    schedule_interval='@daily',  # Runs daily
    start_date=datetime(2025, 1, 1),
    catchup=False,
)

# Define the task
data_quality_task = PythonOperator(
    task_id='run_data_quality_checks',
    python_callable=run_data_quality_checks,
    dag=dag,
)