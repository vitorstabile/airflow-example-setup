from datetime import datetime
from airflow.sdk import dag, task

@dag(
    dag_id="my_test_dag",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["my-tag"],
)
def my_test_dag():

    @task()
    def my_task():
        print("Hello from Airflow 3!")

    my_task()

my_test_dag()
