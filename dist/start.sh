#!/bin/bash

# Navigate to the directory containing the virtual environment
cd ../venv/bin

# Activate the virtual environment
source activate

# Navigate back to the dist directory
cd ../../

# Run the Flask app
python app.py
