import base64
import json
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import os

# Define the base directory
image_directory = "/Users/pastour/Parsa/codes/BI-REX/SISMA_Inference/extracted/13-coperchio_2021_03_24/"

url = "http://192.168.42.29:8080/detect"

with open('BIREX.postman_collection.json', 'r') as file:
    data = json.load(file)

body = json.loads(data['item'][0]['request']['body']['raw'])

for key in body.keys():
    print(key)

username = data['item'][0]['request']['auth']['basic'][0]['value']

password = data['item'][0]['request']['auth']['basic'][1]['value']
