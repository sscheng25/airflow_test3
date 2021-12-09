# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:27:30 2021

@author: CSS
"""

from dotenv import load_dotenv
load_dotenv()

# Import additional required packages
import datetime as dt
import os
import requests
from google.cloud import storage
import json
import pandas as pd

# Retrieve data from URL
print('Downloading the neighborhood data...')
response = requests.get('https://data.cityofchicago.org/resource/y6yq-dbs2.json')

# Save retrieved data to a local file
print('Saving neighborhood data to a file...')

outfile_path = f'neighborhood_{dt.date.today()}.json'
with open(outfile_path, mode='wb') as outfile:
    outfile.write(response.content)


outfile_path1 = f'neighborhood_{dt.date.today()}.csv'
with open(outfile_path, "r") as read_file:
    data = pd.DataFrame(json.load(read_file))
    print(type(data))
    data.to_csv (outfile_path1, index = None)

# Upload local file of data to Google Cloud Storage
print('Uploading neighborhood data to GCS...')
bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
blob_name = f'neighborhood_{dt.date.today()}.csv'

storage_robot = storage.Client()
bucket = storage_robot.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(outfile_path1)

print('Done.')