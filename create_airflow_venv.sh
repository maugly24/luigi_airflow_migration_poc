#!/bin/bash

python3 -m venv airflow_python_venv
. ./airflow_python_venv/bin/activate
pip3 install -r airflow_requirements.txt

