@echo off
setlocal enabledelayedexpansion

REM Define the Python executable path
set python_executable="C:\Users\pnthu\PycharmProjects\check_btstrp\venv\Scripts\python.exe"

REM Define the base command without epsilon range
set base_cmd=%python_executable% ../C_command_line_main.py --data_path "C:\Users\pnthu\PycharmProjects\check_btstrp\data\9_22_2017.csv" --result_path "C:\Users\pnthu\PycharmProjects\check_btstrp\results" --result_file "9_22_2017.csv"

REM Manual commands with small epsilon ranges
%base_cmd% --epsilon_min 0 --epsilon_max 6
%base_cmd% --epsilon_min 6 --epsilon_max 12

%base_cmd% --epsilon_min 12 --epsilon_max 18
%base_cmd% --epsilon_min 18 --epsilon_max 24

%base_cmd% --epsilon_min 24 --epsilon_max 30
%base_cmd% --epsilon_min 30 --epsilon_max 36

%base_cmd% --epsilon_min 36 --epsilon_max 42
%base_cmd% --epsilon_min 42 --epsilon_max 48

%base_cmd% --epsilon_min 48 --epsilon_max 54
%base_cmd% --epsilon_min 54 --epsilon_max 60

pause
