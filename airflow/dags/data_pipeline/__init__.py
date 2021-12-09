from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from pathlib import Path
from pipeline_tools import run_transform_gbq

from . import bus_stop_gcs
from . import crime_gcs
from . import grocery_gcs
from . import neighborhood_gcs
from . import restaurant_gcs
from . import bus_stop_bq
from . import crime_bq
from . import grocery_bq
from . import neighborhood_bq
from . import restaurants_bq

with DAG(dag_id='data_pipeline',
         schedule_interval='@monthly',
         start_date=datetime(2021, 12, 8),
         catchup=False) as dag:

    # EXTRACT TASKS ~~~~~

    bus_stop_gcs_task = PythonOperator(
        task_id='bus_stop_gcs',
        python_callable=bus_stop_gcs.main,
    )
    crime_gcs_task = PythonOperator(
        task_id='crime_gcs',
        python_callable=crime_gcs.main,
    )
    grocery_gcs_task = PythonOperator(
        task_id='grocery_gcs',
        python_callable=grocery_gcs.main,
    )
    neighborhood_gcs_task = PythonOperator(
        task_id='neighborhood_gcs',
        python_callable=neighborhood_gcs.main,
    )
    restaurant_gcs_task = PythonOperator(
        task_id='restaurant_gcs',
        python_callable=restaurant_gcs.main,
    )

    # LOAD TASKS ~~~~~

    bus_stop_bq_task = PythonOperator(
        task_id='bus_stop_bq',
        python_callable=bus_stop_bq.main,
    )
    crime_bq_task = PythonOperator(
        task_id='crime_bq',
        python_callable=crime_bq.main,
    )
    grocery_bq_task = PythonOperator(
        task_id='grocery_bq',
        python_callable=grocery_bq.main,
    )
    neighborhood_bq_task = PythonOperator(
        task_id='neighborhood_bq',
        python_callable=neighborhood_bq.main,
    )
    restaurants_bq_task = PythonOperator(
        task_id='restaurants_bq',
        python_callable=restaurants_bq.main,
    )

    # TRANSFORM TASKS ~~~~~

    sql_dir = Path(__file__).parent / 'sql'

    transform_justtest_average_busstop_task = PythonOperator(
        task_id='transform_justtest_average_busstop',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'average_busstop', sql_dir],
    )
    transform_justtest_average_gro_task = PythonOperator(
        task_id='transform_justtest_average_gro',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'average_gro', sql_dir],
    )
    transform_justtest_average_res_task = PythonOperator(
        task_id='transform_justtest_average_res',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'average_res', sql_dir],
    )
    transform_justtest_boundingbox_task = PythonOperator(
        task_id='transform_justtest_boundingbox',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'boundingbox', sql_dir],
    )
    transform_justtest_bus_in_neigh_task = PythonOperator(
        task_id='transform_justtest_bus_in_neigh',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'bus_in_neigh', sql_dir],
    )
    transform_justtest_bus_stop_level_counts_task = PythonOperator(
        task_id='transform_justtest_bus_stop_level_counts',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'bus_stop_level_counts', sql_dir],
    )
    transform_justtest_centroid_task = PythonOperator(
        task_id='transform_justtest_centroid',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'centroid', sql_dir],
    )
    transform_justtest_count_crimes_oct_task = PythonOperator(
        task_id='transform_justtest_count_crimes_oct',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'count_crimes_oct', sql_dir],
    )
    transform_justtest_count_crimes_task = PythonOperator(
        task_id='transform_justtest_count_crimes',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'count_crimes', sql_dir],
    )
    transform_justtest_count_type_percent_task = PythonOperator(
        task_id='transform_justtest_count_type_percent',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'count_type_percent', sql_dir],
    )
    transform_justtest_cri_in_neigh_task = PythonOperator(
        task_id='transform_justtest_cri_in_neigh',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'cri_in_neigh', sql_dir],
    )
    transform_justtest_crime_risk_task = PythonOperator(
        task_id='transform_justtest_crime_risk',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'crime_risk', sql_dir],
    )
    transform_justtest_gro_in_neigh_task = PythonOperator(
        task_id='transform_justtest_gro_in_neigh',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'gro_in_neigh', sql_dir],
    )
    transform_justtest_gro_level_task = PythonOperator(
        task_id='transform_justtest_gro_level',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'gro_level', sql_dir],
    )
    transform_justtest_max_busstop_task = PythonOperator(
        task_id='transform_justtest_max_busstop',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'max_busstop', sql_dir],
    )
    transform_justtest_max_crime_task = PythonOperator(
        task_id='transform_justtest_max_crime',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'max_crime', sql_dir],
    )
    transform_justtest_max_gro_task = PythonOperator(
        task_id='transform_justtest_max_gro',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'max_gro', sql_dir],
    )
    transform_justtest_max_res_task = PythonOperator(
        task_id='transform_justtest_max_res',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'max_res', sql_dir],
    )
    transform_justtest_min_busstop_task = PythonOperator(
        task_id='transform_justtest_min_busstop',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'min_busstop', sql_dir],
    )
    transform_justtest_min_crime_task = PythonOperator(
        task_id='transform_justtest_min_crime',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'min_crime', sql_dir],
    )
    transform_justtest_min_gro_task = PythonOperator(
        task_id='transform_justtest_min_gro',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'min_gro', sql_dir],
    )
    transform_justtest_min_res_task = PythonOperator(
        task_id='transform_justtest_min_res',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'min_res', sql_dir],
    )
    transform_justtest_neighborhood_list_task = PythonOperator(
        task_id='transform_justtest_neighborhood_list',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'neighborhood_list', sql_dir],
    )
    transform_justtest_nhoods_detail_task = PythonOperator(
        task_id='transform_justtest_nhoods_detail',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'nhoods_detail', sql_dir],
    )
    transform_justtest_nhoods_index_task = PythonOperator(
        task_id='transform_justtest_nhoods_index',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'nhoods_index', sql_dir],
    )
    transform_justtest_num_percent_crime_oct_task = PythonOperator(
        task_id='transform_justtest_num_percent_crime_oct',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'num_percent_crime_oct', sql_dir],
    )
    transform_justtest_res_in_neigh_task = PythonOperator(
        task_id='transform_justtest_res_in_neigh',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'res_in_neigh', sql_dir],
    )
    transform_justtest_res_level_task = PythonOperator(
        task_id='transform_justtest_res_level',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'res_level', sql_dir],
    )
    transform_justtest_total_busstop_task = PythonOperator(
        task_id='transform_justtest_total_busstop',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'total_busstop', sql_dir],
    )
    transform_justtest_total_crime_task = PythonOperator(
        task_id='transform_justtest_total_crime',
        python_callable=run_transform_gbq,
        op_args=['justtest', 'total_crime', sql_dir],
    )

    # DEPENDENCIES ~~~~~

    bus_stop_gcs_task >> bus_stop_bq_task
    crime_gcs_task >> crime_bq_task
    grocery_gcs_task >> grocery_bq_task
    neighborhood_gcs_task >> neighborhood_bq_task
    restaurant_gcs_task >> restaurants_bq_task
    

    load_tasks = DummyOperator(task_id='wait_for_loads')
    load_tasks << [
        bus_stop_bq_task,
        crime_bq_task,
        grocery_bq_task,
        neighborhood_bq_task,
        restaurants_bq_task,
    ]

    transform_justtest_average_busstop_task << load_tasks
    transform_justtest_average_gro_task << load_tasks
    transform_justtest_average_res_task << load_tasks
    transform_justtest_boundingbox_task << load_tasks
    transform_justtest_bus_in_neigh_task << load_tasks
    transform_justtest_bus_stop_level_counts_task << load_tasks
    transform_justtest_centroid_task << load_tasks
    transform_justtest_count_crimes_oct_task << load_tasks      
    transform_justtest_count_crimes_task << load_tasks
    transform_justtest_count_type_percent_task << load_tasks
    transform_justtest_cri_in_neigh_task << load_tasks
    transform_justtest_crime_risk_task << load_tasks
    transform_justtest_gro_in_neigh_task << load_tasks
    transform_justtest_gro_level_task << load_tasks
    transform_justtest_max_busstop_task << load_tasks
    transform_justtest_max_crime_task << load_tasks
    transform_justtest_max_gro_task << load_tasks
    transform_justtest_max_res_task << load_tasks
    transform_justtest_min_busstop_task << load_tasks
    transform_justtest_min_crime_task << load_tasks
    transform_justtest_min_gro_task << load_tasks
    transform_justtest_min_res_task << load_tasks
    transform_justtest_neighborhood_list_task << load_tasks
    transform_justtest_nhoods_detail_task << load_tasks
    transform_justtest_nhoods_index_task << load_tasks
    transform_justtest_num_percent_crime_oct_task << load_tasks
    transform_justtest_res_in_neigh_task << load_tasks
    transform_justtest_res_level_task << load_tasks
    transform_justtest_total_busstop_task << load_tasks
    transform_justtest_total_crime_task << load_tasks
   