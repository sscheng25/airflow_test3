# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:37:37 2021

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

print('Downloading grocery data...')

client = Socrata("data.cityofchicago.org", None)
results = client.get("53t8-wyrc", limit=1000)

# pd.set_option('display.max_columns', None)
results_df = pd.DataFrame.from_records(results)
# results_df.head()

results = pd.DataFrame(results, columns=[
    'store_name', 'license_id', 'square_feet', 'buffer_size',
    'address', 'zip_code', 'census_tract', 'census_block', 
    'latitude', 'longitude'])
results.to_csv(f'grocery_{dt.date.today()}.csv', index=False)

# Upload local file of data to Google Cloud Storage
print('Uploading grocery data to GCS...')
bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
blob_name = f'grocery_{dt.date.today()}.csv'
outfile_path1 = f'grocery_{dt.date.today()}.csv'

storage_robot = storage.Client()
bucket = storage_robot.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(outfile_path1)

print('Done.')