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
urls_path = '/home/tommi/vscode-projects/pinterest-data-pipeline693/credentials/aws_urls.yaml'
headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

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
        
    with open(urls_path, 'r') as url_strings:
        api_urls = yaml.safe_load(url_strings)

        pin_invoke_url = api_urls['pin_invoke_url']
        geo_invoke_url = api_urls['geo_invoke_url']
        user_invoke_url = api_urls['user_invoke_url']

    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)

            for row in pin_selected_row:
                pin_result = dict(row._mapping)
                pin_payload = json.dumps({"records": [{"value": pin_result}]}, default=str)
                pin_response = requests.request("POST", pin_invoke_url, headers=headers, data=pin_payload)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)

            for row in geo_selected_row:
                geo_result = dict(row._mapping)
                geo_payload = json.dumps({"records": [{"value": geo_result}]}, default=str)
                geo_response = requests.request("POST", geo_invoke_url, headers=headers, data=geo_payload)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
                user_payload = json.dumps({"records": [{"value": user_result}]}, default=str)
                user_response = requests.request("POST", user_invoke_url, headers=headers, data=user_payload)
            
            print(pin_response.status_code)
            print(geo_response.status_code)
            print(user_response.status_code)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')