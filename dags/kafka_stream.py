from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator

import json
import requests
import logging

@dag(
    dag_id = "user_automation",
    schedule = "@daily",
    start_date = datetime(2025, 2, 15, 12, 0),
    catchup = False
)
def user_automation():

    start_task = EmptyOperator(task_id="start")

    @task(task_id="streaming_task")
    def stream_data():
        """Fetch random users from the API. """

        response = requests.get('https://randomuser.me/api/').json()
        #logging.info(f"The users its ${response}")
        print(response)
    
    start_task >> stream_data()

user_automation()