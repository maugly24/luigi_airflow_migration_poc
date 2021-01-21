#!/bin/bash

python3 -m venv luigi_python_venv
. ./luigi_python_venv/bin/activate
pip3 install -r luigi_requirements.txt
cp example_luigi.py luigi_python_venv/lib/python3.7/site-packages/
cp files_test_luigi.py luigi_python_venv/lib/python3.7/site-packages/

