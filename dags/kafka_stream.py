from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator

import requests
import logging
import json

@dag(
    dag_id = "user_automation",
    schedule = "@daily",
    start_date = datetime(2025, 2, 15, 12, 0),
    catchup = False
)
def user_automation():

    start_task = EmptyOperator(task_id="start")

    @task(task_id="get_data_task")
    def get_data():
        """Fetch random users from the API. """

        response = requests.get('https://randomuser.me/api/').json()
        res = response['results'][0]
        logging.info(f"The first user it's ${res}")
        print(json.dumps(res, indent=3))

        return res

    @task(task_id="format_data_task")
    def format_data(res):
        """Fetch random users from the API. """
        data = {}
        location = res['location']
        data['first_name'] = res['name']['first']
        data['last_name'] = res['name']['last']
        data['gender'] = res['gender']
        data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                            f"{location['city']}, {location['state']}, {location['country']}"
        data['post_code'] = location['postcode']
        data['email'] = res['email']
        data['username'] = res['login']['username']
        data['dob'] = res['dob']['date']
        data['registered_date'] = res['registered']['date']
        data['phone'] = res['phone']
        data['picture'] = res['picture']['medium']

        return data
    
    @task(task_id="streaming_task")
    def stream_data(res):
        """Fetch random users from the API. """
        pass

    data = get_data()
    data = format_data(data)
    start_task >> stream_data(data)

user_automation()