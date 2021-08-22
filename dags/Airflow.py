from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    'weather_prediction_airflow',
    default_args=default_args,
    description='weather_prediction',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(5),
    tags=['weather'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )
    
    t2 = BashOperator(
    task_id='install_reqs',
    bash_command='pip install -r DIRECTORY',
    dag=dag)
    
    t3 = BashOperator(
    task_id='weather_airflow',
    bash_command='python DIRECTORY',
    dag=dag)

    # )
    # t1.doc_md = dedent(
    #     """\
    # #### Task Documentation
    # You can document your task using the attributes `doc_md` (markdown),
    # `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    # rendered in the UI's Task Instance Details page.
    # ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

    # """
    # )

    # dag.doc_md = __doc__  # providing that you have a docstring at the beggining of the DAG
    # dag.doc_md = """
    # This is a documentation placed anywhere
    # """  # otherwise, type it like this
    # templated_command = dedent(
    #     """
    # {% for i in range(5) %}
    #     echo "{{ ds }}"
    #     echo "{{ macros.ds_add(ds, 7)}}"
    #     echo "{{ params.my_param }}"
    # {% endfor %}
    # """
    # )

    # t3 = BashOperator(
    #     task_id='templated',
    #     depends_on_past=False,
    #     bash_command=templated_command,
    #     params={'my_param': 'Parameter I passed in'},
    # )
    
    # t1 >> [t2, t3]
    t1 >> t2 >> t3