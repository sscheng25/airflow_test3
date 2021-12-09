from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv()
import datetime as dt
import os
from google.cloud import storage

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "INTEGER"),
        bigquery.SchemaField("case_number", "STRING"),
        bigquery.SchemaField("date", "DATETIME"),
        bigquery.SchemaField("primary_type", "STRING"),
        bigquery.SchemaField("description", "STRING"),
        bigquery.SchemaField("district", "STRING"),
        bigquery.SchemaField("year", "INTEGER"),
        bigquery.SchemaField("latitude", "FLOAT"),
        bigquery.SchemaField("longitude", "FLOAT"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)


bucket_name = os.environ['PIPELINE_DATA_BUCKET']
blob_name = f'crime_{dt.date.today()}.csv'
uri = 'gs://%s/%s' % (bucket_name, blob_name)

table_id = f'musa-509-final.justtest.crime_{dt.date.today()}'

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))