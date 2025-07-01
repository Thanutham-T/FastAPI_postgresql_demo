@echo off
REM Activate virtual environment if you have one:
REM Uncomment and edit the line below with your venv path if needed:
call .\.venv\Scripts\activate

REM Run FastAPI with the development server
fastapi dev .\src\FastAPI_postgresql_demo\main.py

pause
