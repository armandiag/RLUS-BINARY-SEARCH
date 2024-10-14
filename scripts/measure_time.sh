#!/bin/bash

# Log file to store the computation time
log_file="/app/scripts/master_script_time.log"

# Clear the log file if it already exists
> $log_file

# Measure and log the execution time of the master script
{ time bash /app/scripts/master_script.sh; } 2>> $log_file

echo "Master script execution time has been logged to $log_file."
