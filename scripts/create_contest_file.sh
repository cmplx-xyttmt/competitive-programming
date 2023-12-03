#!/usr/bin/env bash

# Run
#   create_contest_file filename1.py filename2.py ...
# to create files that read from standard input and write to standard output
# Add a --file flag to create python files that read input from files.

contest_task='~/Projects/competitive-programming/python/src/contest_task_template.py'
file_contest_task='~/Projects/competitive-programming/python/src/file_contest_task_template.py'
task_type='std'
for argument in $@; do
#    cp ~/Projects/competitive-programming/python/src/contest_task_template.py $filename
    if [[ $argument == "--file" ]]; then
        task_type='file'
    else
        if [[ $task_type == "file" ]]; then
            cp ~/Projects/competitive-programming/python/src/file_contest_task_template.py $argument
        else
            cp ~/Projects/competitive-programming/python/src/contest_task_template.py $argument
        fi
    fi
done
