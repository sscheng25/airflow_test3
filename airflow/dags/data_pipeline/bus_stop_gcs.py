# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:33:26 2021

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

def main():
    print('Downloading bus stop data...')

    client = Socrata("data.cityofchicago.org", None)
    results = client.get("qs84-j7wh", limit=12000)

    # pd.set_option('display.max_columns', None)
    results_df = pd.DataFrame.from_records(results)
    # results_df.head()

    results = pd.DataFrame(results, columns=[
        'systemstop', 'objectid', 'street', 'routesstpg',
        'public_nam', 'point_x', 'point_y'])
    results.to_csv(f'bus_stop_{dt.date.today()}.csv', index=False)

    # Upload local file of data to Google Cloud Storage
    print('Uploading bus stop data to GCS...')
    bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
    blob_name = f'bus_stop_{dt.date.today()}.csv'
    outfile_path1 = f'bus_stop_{dt.date.today()}.csv'

    storage_robot = storage.Client()
    bucket = storage_robot.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(outfile_path1)

    print('Done.')



    """
    # Retrieve data from URL
    print('Downloading the bus stop data...')
    response = requests.get('https://data.cityofchicago.org/resource/qs84-j7wh.json')

    # Save retrieved data to a local file
    print('Saving bus stop data to a file...')

    outfile_path = f'bus_stop_{dt.date.today()}.json'
    with open(outfile_path, mode='wb') as outfile:
        outfile.write(response.content)


    outfile_path1 = f'bus_stop_{dt.date.today()}.csv'
    with open(outfile_path, "r") as read_file:
        data = pd.DataFrame(json.load(read_file))
        print(type(data))
        data.to_csv (outfile_path1, index = None)

    # Upload local file of data to Google Cloud Storage
    print('Uploading bus stop data to GCS...')
    bucket_name = os.environ['PIPELINE_DATA_BUCKET']  # <-- retrieve the bucket name from the environment
    blob_name = f'bus_stop_{dt.date.today()}.csv'

    storage_robot = storage.Client()
    bucket = storage_robot.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(outfile_path1)

    print('Done.')

    """
if __name__=='__main__':
    main()