#!/bin/bash

# Enable debug mode
sed -i 's/DEBUG = False/DEBUG = True/' config/settings.py


# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Start the server
python3 manage.py runserver
