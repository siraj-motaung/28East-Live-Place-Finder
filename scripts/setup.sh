#!/bin/bash

echo "Starting setup..."

# 1. Create the virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# 2. ACTIVATE the environment
echo "Activating virtual environment..."
source venv/bin/activate

# 3. Upgrade pip inside the active venv
echo "Upgrading pip..."
pip install --upgrade pip

# 4. Install the requirements
echo "Installing requirements from live_place_finder_api/requirements.txt..."
if [ -f "live_place_finder_api/requirements.txt" ]; then
    pip install -r live_place_finder_api/requirements.txt
    echo "Requirements installed successfully!"
else
    echo "Error: live_place_finder_api/requirements.txt not found."
    exit 1
fi

echo "---"
echo "✅ Setup complete!"
echo "To start working, you MUST run this command in your terminal:"
echo "source venv/bin/activate"

echo "🚀 Starting Flask Server..."
python live_place_finder_api/app.py
