# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:45:10 2021

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
from sodapy import Socrata

print('Downloading crime data...')

client = Socrata("data.cityofchicago.org", None)
results = client.get("ijzp-q8t2", limit=20000)

# pd.set_option('display.max_columns', None)
results_df = pd.DataFrame.from_records(results)
# results_df.head()

results = pd.DataFrame(results, columns=[
    'id', 'case_number', 'date', 'primary_type',
    'description', 'district', 'year', 'latitude', 
    'longitude'])
results.to_csv(f'crime_{dt.date.today()}.csv', index=False)

# Upload local file of data to Google Cloud Storage
print('Uploading crime data to GCS...')
bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
blob_name = f'crime_{dt.date.today()}.csv'
outfile_path1 = f'crime_{dt.date.today()}.csv'

storage_robot = storage.Client()
bucket = storage_robot.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(outfile_path1)

print('Done.')

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
print('Downloading crime data...')
response = requests.get('https://data.cityofchicago.org/resource/ijzp-q8t2.json')

# Save retrieved data to a local file
print('Saving crime data to a file...')

outfile_path = f'crime_{dt.date.today()}.json'
with open(outfile_path, mode='wb') as outfile:
    outfile.write(response.content)


outfile_path1 = f'crime_{dt.date.today()}.csv'
with open(outfile_path, "r") as read_file:
    data = pd.DataFrame(json.load(read_file))
    print(type(data))
    data.to_csv (outfile_path1, index = None)

# Upload local file of data to Google Cloud Storage
print('Uploading crime data to GCS...')
bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
blob_name = f'crime_{dt.date.today()}.csv'

storage_robot = storage.Client()
bucket = storage_robot.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(outfile_path1)

print('Done.')
"""