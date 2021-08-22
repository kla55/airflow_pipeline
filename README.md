# airflow_pipeline

In conjuntion with the weather ARIMA model, the airflow pipeline uses a manage, monitor and execute a workflow. In this pipeline, it use a simple DAG to schedule task required for the model to generate an output.
The folder contains the basic elements of the airflow pipeline locally.


To run, needs to perform the following:

1. Install airflow
2. Create a home for airflow
3. Create virtual environment
4. Modify dag file in relation to the model generated
5. Create requirements textfile if necessary
6. Run command "airflow scheduler" >> updates DAG list and will run any active DAGs
7. Run command "airflow webservice" >> go to localhost:8080 >> base UI of airflow, can rerun DAGs, visual comparison, logs evaluations, remove dags


** NEED TO SET DIRECTORY **

Resources:
https://www.kdnuggets.com/2021/03/build-dag-factory-airflow.html \
https://towardsdatascience.com/a-complete-introduction-to-apache-airflow-b7e238a33df \ 
https://marclamberti.com/blog/airflow-dag-creating-your-first-dag-in-5-minutes/ \
https://towardsdatascience.com/master-apache-airflow-write-your-first-dag-with-python-in-minutes-6c50b5d4aab1
