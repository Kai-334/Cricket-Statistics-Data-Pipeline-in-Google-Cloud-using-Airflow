from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 12, 7),
    'depends_on_past': False,
    'email': ['lszekai977@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Creates a DAG object named employee_data
# passes the default_args dictionary to the DAG
# Airflow will not backfill missing runs for previous days
dag = DAG('fetch_cricket_stats',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

# Executes a bash command to run a python script at a specified location
with dag:
    run_script_task = BashOperator(
        task_id='run_script',
        bash_command='python /home/airflow/gcs/dags/scripts/extract_and_upload.py',
    )