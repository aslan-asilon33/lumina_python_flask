REM open cmd not PowerShell
cls
call .venv\Scripts\activate.bat

pip list

flask --app app run

