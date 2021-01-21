from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow import DAG
from datetime import timedelta
from glob import glob
import airflow
import gzip
import shutil

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='files_test_dag', default_args=args,
    schedule_interval='* * * * *',
    dagrun_timeout=timedelta(minutes=60))


def extract_gzs():
    for filename in glob('*.gz'):
        print(filename)
        with gzip.open(filename, 'rb') as f_in, open(filename+'.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def wc_script():
    for filename in glob('*.gz.txt'):
        print(filename)
        with open(filename, 'r') as f_in, open(filename+'.count', 'w') as f_out:
            print(len(f_in.read().splitlines()), file=f_out)


extractGZ = PythonOperator(
        task_id='extract_gz',
        provide_context=True,
        python_callable=extract_gzs,
        dag=dag,)


wc_script = PythonOperator(
        task_id='wc_script', 
        provide_context=True,
        python_callable=wc_script,
        dag=dag,)


extractGZ.set_downstream(wc_script)
# extractGZ >> wc_script

if __name__ == "__main__":
    dag.cli()
