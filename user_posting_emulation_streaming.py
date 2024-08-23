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

creds_path = '/home/tommi/vscode-projects/pinterest-data-pipeline693/credentials/db_creds.yaml'

pin_invoke_url = "https://aj3ii03bub.execute-api.us-east-1.amazonaws.com/test/streams/streaming-0affea73130b-pin/record"
geo_invoke_url = "https://aj3ii03bub.execute-api.us-east-1.amazonaws.com/test/streams/streaming-0affea73130b-geo/record"
user_invoke_url = "https://aj3ii03bub.execute-api.us-east-1.amazonaws.com/test/streams/streaming-0affea73130b-user/record"

headers = {'Content-Type': 'application/json'}

class AWSDBConnector:

    def __init__(self):

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
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)

            for row in pin_selected_row:
                pin_result = dict(row._mapping)
                pin_payload = json.dumps({
                    "StreamName": "YourStreamName",
                    "Data": pin_result,
                        "PartitionKey": "partition-1"
                        }, default=str)
                pin_response = requests.request("PUT", pin_invoke_url, headers=headers, data=pin_payload)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)

            for row in geo_selected_row:
                geo_result = dict(row._mapping)
                geo_payload = json.dumps({
                    "StreamName": "YourStreamName",
                    "Data": geo_result,
                        "PartitionKey": "partition-1"
                        }, default=str)
                geo_response = requests.request("PUT", geo_invoke_url, headers=headers, data=geo_payload)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
                user_payload = json.dumps({
                    "StreamName": "YourStreamName",
                    "Data": user_result,
                        "PartitionKey": "partition-1"
                        }, default=str)
                user_response = requests.request("PUT", user_invoke_url, headers=headers, data=user_payload)
            

            print(pin_response.status_code)
            print(geo_response.status_code)
            print(user_response.status_code)
            print('Working')

if __name__ == "__main__":
    run_infinite_post_data_loop()