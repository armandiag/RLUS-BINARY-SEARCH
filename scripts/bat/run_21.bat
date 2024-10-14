@echo off
setlocal enabledelayedexpansion

REM Define the Python executable path
set "python_executable=C:\Users\pnthu\PycharmProjects\check_btstrp_bruteforce_final\venv\Scripts\python.exe"

REM Define the full command with all parameters
set "full_cmd=!python_executable! C:\Users\pnthu\PycharmProjects\check_btstrp_bruteforce_final\C_command_line_main.py --data_path C:\Users\pnthu\PycharmProjects\check_btstrp_bruteforce_final\data\9_21_2017.csv --result_path C:\Users\pnthu\PycharmProjects\check_btstrp_bruteforce_final\results --result_file 9_21_2017.csv --epsilon_min 0 --epsilon_max 6"

REM Execute the command
echo Running the script...
!full_cmd!

echo Script execution completed.
pause
