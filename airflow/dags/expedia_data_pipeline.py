from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    'expedia_data_pipeline',
    default_args=default_args,
    description='A simple tutorial DAG for Expedia data processing',
    schedule_interval='@daily',
    start_date=days_ago(1),
    tags=['expedia'],
) as dag:

    # Define tasks
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    # Define task dependency
    start >> end
