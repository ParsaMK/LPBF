import base64
import json
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import os
import time
from tqdm import tqdm
import re

IMAGE_DIRECTORY_NAME = "23-2021_04_07_Coperchi 2"

# Define the base directory
image_directory = f"extracted/{IMAGE_DIRECTORY_NAME}"

url = "http://192.168.42.29:8080/detect"

with open('BIREX.postman_collection.json', 'r') as file:
    data = json.load(file)

body = json.loads(data['item'][0]['request']['body']['raw'])

username = data['item'][0]['request']['auth']['basic'][0]['value']

password = data['item'][0]['request']['auth']['basic'][1]['value']

# Create a DataFrame if it doesn't already exist
try:
    # Try to load an existing DataFrame from a CSV file
    df = pd.read_csv('inference.csv')
except FileNotFoundError:
    # If the file does not exist, create a new DataFrame
    df = pd.DataFrame(columns=['LayerID','Anomalous', 'Area'])  # Define columns as needed

# Function to perform natural sorting
def natural_sort_key(s):
    # Split the filename into numeric and non-numeric parts
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# List all files and remove extensions for sorting
files = [f for f in os.listdir(image_directory) if f.endswith(".jpeg")]
files_no_ext = [os.path.splitext(f)[0] for f in files]

# Sort the files naturally based on their names without extensions
sorted_files_no_ext = sorted(files_no_ext, key=natural_sort_key)

start_time = time.time()
# Loop through the sorted filenames without extensions
for filename_no_ext in tqdm(sorted_files_no_ext):
    filename = filename_no_ext + ".jpeg"
    image_path = os.path.join(image_directory, filename)
    # Open the image file and convert it to Base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        body["imgData"] = encoded_string
        response = requests.post(url, json=body, auth=HTTPBasicAuth(username, password))
        data = response.json()

        # Extract the boundingBoxes
        bounding_boxes = data.get("boundingBoxes", [])

        # Check if boundingBoxes is not empty and add a row if it is not
        if bounding_boxes:  # This checks if the list is not empty
            area = 0
            for box in bounding_boxes:
                # Extract the area of the bounding box
                area += (float(box['height']) * float(box['width']))
            # Create a new row as a DataFrame
            new_row = pd.DataFrame({'LayerID': [filename_no_ext], 'Anomalous': [1], 'Area': [area]})
            # Append the new row using pd.concat
            df = pd.concat([df, new_row], ignore_index=True)
        else:
            # Create a new row as a DataFrame
            new_row = pd.DataFrame({'LayerID': [filename_no_ext], 'Anomalous': [0], 'Area': [0]})
            # Append the new row using pd.concat
            df = pd.concat([df, new_row], ignore_index=True)

        # Save the DataFrame to a CSV file
        df.to_csv(f'./Inferences/{IMAGE_DIRECTORY_NAME}_inference.csv', index=False)

end_time = time.time()

time_elapsed = end_time - start_time

print(f"Time taken: {time_elapsed} seconds")
print(f"Around {time_elapsed/len(sorted_files_no_ext)} seconds per image on average")


