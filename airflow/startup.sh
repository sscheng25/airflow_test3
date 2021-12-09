#!/bin/bash

# Get this scripts folder
AIRFLOW_DIR=$(dirname $0)

# Load the environment variables
source ${AIRFLOW_DIR}/env.sh

# Stop any currently running Airflow processes
pkill airflow

# Start the scheduler and the webserver
nohup airflow scheduler >> scheduler.$(date -I).log &
nohup airflow webserver -p 8080 >> webserver.$(date -I).log &
