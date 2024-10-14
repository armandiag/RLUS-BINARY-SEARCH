#!/bin/bash

# Define the Python executable path
python_executable="/usr/local/bin/python3"

# Define the base command without epsilon range
base_cmd="$python_executable /app/C_command_line_main.py --data_path /app/data/9_21_2017.csv --result_path /app/results --result_file 9_21_2017.csv"

# Log file path
log_file="/app/logs/run_21_time_log.txt"

# Function to log execution time and check command success
log_time() {
    echo "Running command with epsilon range $2"
    start_time=$(date +%s.%N)  # Get start time in seconds with nanosecond precision
    eval "$1"
    status=$?
    end_time=$(date +%s.%N)  # Get end time in seconds with nanosecond precision
    duration=$(awk "BEGIN{print $end_time - $start_time}")  # Calculate duration using awk
    log_message="Time taken for range $2: ${duration} seconds"
    echo $log_message >> $log_file
    if [ $status -ne 0 ]; then
        echo "Command failed with epsilon range $2"
        echo $log_message " - FAILED" >> $log_file
        exit 1
    fi
}

# Ensure the log directory exists and is writable
mkdir -p $(dirname $log_file)
chmod u+w $(dirname $log_file)

# Manual commands with small epsilon ranges
log_time "$base_cmd --epsilon_min 0 --epsilon_max 6" "0-6"
log_time "$base_cmd --epsilon_min 6 --epsilon_max 12" "6-12"
log_time "$base_cmd --epsilon_min 12 --epsilon_max 18" "12-18"
log_time "$base_cmd --epsilon_min 18 --epsilon_max 24" "18-24"
log_time "$base_cmd --epsilon_min 24 --epsilon_max 30" "24-30"
log_time "$base_cmd --epsilon_min 30 --epsilon_max 36" "30-36"
log_time "$base_cmd --epsilon_min 36 --epsilon_max 42" "36-42"
log_time "$base_cmd --epsilon_min 42 --epsilon_max 48" "42-48"
log_time "$base_cmd --epsilon_min 48 --epsilon_max 54" "48-54"
log_time "$base_cmd --epsilon_min 54 --epsilon_max 60" "54-60"
