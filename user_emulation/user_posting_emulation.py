import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
import yaml

random.seed(100)

creds_path = '../credentials/db_creds.yaml'
urls_path = '../credentials/aws_urls.yaml'
headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

class AWSDBConnector:

    def __init__(self):
        # load db credentials
        with open(creds_path, 'r') as creds:
            db_creds = yaml.safe_load(creds)

        self.HOST = db_creds['HOST']
        self.USER = db_creds['USER']
        self.PASSWORD = db_creds['PASSWORD']
        self.DATABASE = db_creds['DATABASE']
        self.PORT = db_creds['PORT']
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()


def run_infinite_post_data_loop():
    # retrieve api invoke urls
    with open(urls_path, 'r') as api_urls:
        invoke_urls = yaml.safe_load(api_urls)

    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            for value in invoke_urls:
                sql_string = text(f"SELECT * FROM {value} LIMIT {random_row}, 1")
                selected_row = connection.execute(sql_string)

                for row in selected_row:
                    sql_result = dict(row._mapping)
                    api_payload = json.dumps({"records": [{"value": sql_result}]}, default=str)
                    api_response = requests.request("POST", invoke_urls[value], headers=headers, data=api_payload)

                if api_response.status_code != 200:
                    print(f"Failed to send data. Status code: {api_response.status_code}")
                else:
                    print(f"Successfully sent data.Status code: {api_response.status_code}")
                    print(api_payload)

        print('Working')


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print("Loop end.")
