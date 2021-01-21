rm 500*_lines*
./generate_inputs.sh
. create_airflow_venv.sh
cp files_test_airflow.py ~/airflow/dags/files_test_airflow.py
#airflow tasks test files_test_dag extract_gz 2020-02-02
airflow dags test files_test_dag 2020-02-02
deactivate

