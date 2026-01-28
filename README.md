# 28East-Live-Place-Finder
A full-stack web application for 28East that identifies nearby points of interest. Features a Python Flask backend orchestrating Google Maps Geocoding and Places APIs to transform user addresses into interactive map markers and detailed location lists. Demonstrates API orchestration, clean UI design, and asynchronous JavaScript.


## 🚀 Getting Started
### 1. Set Your Google API Key
To authenticate with Google Maps services, you must export your API key to your terminal session. Replace the placeholder text with your actual key:
```
export GOOGLE_API_KEY="your_actual_api_key_here"
```

### 2. Run the Setup & Start Script
The project includes a unified script that handles environment creation, dependency installation, and server startup. Run the following command:
```
source scripts/setup.sh
```


## Manual Installation (Alternative)
If you prefer to run the steps manually or if the script fails, use these commands:

### 1. Create and Activate Virtual Environment:

```
python3 -m venv venv
source venv/bin/activate
```
### 2. Install Dependencies:
```
pip install -r requirements.txt
```
### 3. Start the Flask Server:
```
python app.py
```

# 📂 Project Structure
```
├── app.py              # Flask server & API integration logic
├── scripts/
│   └── setup.sh        # Automated venv creation and port cleanup
├── static/
│   ├── main.js         # Frontend logic, Map handling, and UI updates
│   └── style.css       # Custom CSS and styling
├── templates/
│   └── index.html      # Main application dashboard
└── requirements.txt    # Python dependencies
```
## ⚠️ Troubleshooting
Port 5000/5001 is busy: The setup.sh script automatically attempts to kill processes occupying the necessary port but you can also do it manually:
```
kill -9 $(lsof -t -i:5000)
```

Permission Denied: If you cannot run the script, grant execution permissions first:
```
chmod +x scripts/setup.sh
```

Map Not Loading: Ensure the API key exported in Step 1 has the "Maps JavaScript API" and "Places API" enabled in your Google Cloud Console.
