# Airflow configuration vars
export AIRFLOW_HOME=$HOME/airflow
export AIRFLOW_DB_PASSWORD='...'
export AIRFLOW_DB_IPADDR='...'
export AIRFLOW__CORE__EXECUTOR=LocalExecutor
export AIRFLOW__CORE__PARALLELISM=1
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:${AIRFLOW_DB_PASSWORD}@${AIRFLOW_DB_IPADDR}/postgres
export AIRFLOW__CORE__FERNET_KEY=''
export AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION='true'
export AIRFLOW__CORE__LOAD_EXAMPLES='false'
export AIRFLOW__WEBSERVER__WORKERS=3
export AIRFLOW__API__AUTH_BACKEND='airflow.api.auth.backend.basic_auth'

# Pipeline script vars
export PIPELINE_PROJECT='...'
export PIPELINE_DATA_BUCKET='...'
export PIPELINE_DATASET='...'
export GOOGLE_APPLICATION_CREDENTIALS=${HOME}/google-app-creds.json
