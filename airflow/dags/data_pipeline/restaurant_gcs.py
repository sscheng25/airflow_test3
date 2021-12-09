# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:12:22 2021

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

print('Downloading restaurant data...')

client = Socrata("data.cityofchicago.org", None)
results = client.get("4ijn-s7e5", limit=250000)

# pd.set_option('display.max_columns', None)
results_df = pd.DataFrame.from_records(results)
# results_df.head()

results = pd.DataFrame(results, columns=[
    'inspection_id', 'dba_name', 'license_', 'facility_type',
    'address', 'zip', 'latitude', 
    'longitude'])
results.to_csv(f'restaurant_{dt.date.today()}.csv', index=False)

# Upload local file of data to Google Cloud Storage
print('Uploading restaurant data to GCS...')
bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
blob_name = f'restaurant_{dt.date.today()}.csv'
outfile_path1 = f'restaurant_{dt.date.today()}.csv'

storage_robot = storage.Client()
bucket = storage_robot.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(outfile_path1)

print('Done.')
