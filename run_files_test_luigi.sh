rm 500*_lines*
./generate_inputs.sh
. create_luigi_venv.sh
luigi --module files_test_luigi TestTask
deactivate

