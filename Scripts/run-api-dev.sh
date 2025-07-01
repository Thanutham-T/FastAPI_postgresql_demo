#!/bin/bash
# Activate virtual environment if you have one:
source ./.venv/bin/activate

# Run FastAPI with the development server
fastapi dev ./src/FastAPI_postgresql_demo/main.py
