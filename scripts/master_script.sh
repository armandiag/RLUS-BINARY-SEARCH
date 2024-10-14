#!/bin/bash

# Run all scripts in parallel
/app/scripts/run_20.sh &
/app/scripts/run_21.sh &
/app/scripts/run_22.sh &
/app/scripts/run_23.sh &
/app/scripts/run_24.sh &
/app/scripts/run_25.sh &
/app/scripts/run_26.sh &
/app/scripts/run_27.sh &
/app/scripts/run_28.sh &
/app/scripts/run_29.sh &

# Wait for all background jobs to finish
wait	