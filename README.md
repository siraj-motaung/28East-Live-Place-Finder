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

### 3. Accessing the Application
Once the script successfully starts the server, you will see a message in your terminal like this:
`* Running on http://127.0.0.1:5000`

To view your app, copy and paste the following URL into your web browser:  
```
http://127.0.0.1:5000
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

### 4. Accessing the Application
Once the script successfully starts the server, you will see a message in your terminal like this:
`* Running on http://127.0.0.1:5000`

To view your app, copy and paste the following URL into your web browser:  
```
http://127.0.0.1:5000
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
Port 5000 is busy: The setup.sh script automatically attempts to kill processes occupying the necessary port, but you can also do it manually:
```
kill -9 $(lsof -t -i:5000)
```

Permission Denied: If you cannot run the script, grant execution permissions first:
```
chmod +x scripts/setup.sh
```

Map Not Loading: Ensure the API key exported in Step 1 has the "Maps JavaScript API" and "Places API" enabled in your Google Cloud Console.

# 🛠 AI-Assistance & Research Disclosure
In accordance with the assessment guidelines, I am simply disclosing the use of AI (Gemini) as a research and boilerplate aid for this project.

## 1. Conceptual Understanding & Research
I used AI as a supplemental learning tool alongside official documentation to quickly grasp the following Google Maps Platform concepts:
- Geocoding API: Understanding how to parse JSON responses to extract specific lat and lng coordinates from a user's address.
- Places API (Nearby Search): Learning the required parameters (location, radius, and type) to center a search on specific coordinates.
- Maps JavaScript API: Understanding how to initialize a map, manage markers, and link the frontend display to backend data.
  
  - Why: I used these tools to quickly bridge the gap between my existing knowledge and the specific requirements of the Google Maps Platform. Using AI as a "technical tutor" allowed me to understand the data structures (JSON) and parameters (radius, location types) required to ensure the backend and frontend were perfectly synced. 

## 2. Core Logic (Authored by Me)
- API Orchestration (app.py): I designed the logic flow to handle the two-step dependency between Google’s services:
   - Step 1 (Geocoding): I implemented the request to the Geocoding API to transform a user's plain-text address into a coordinate object. I manually extracted the specific latitude and longitude from the nested JSON response: results[0]['geometry']['location'].
   - Step 2 (Nearby Search): I used the coordinates retrieved from Step 1 to dynamically populate the location parameter of the Places API. This ensures the search is mathematically centered on the user's input before returning the results to the frontend.

- Asynchronous Frontend (main.js): I developed the fetch logic and the marker management system. I wrote the logic to clear previous markers from the markers array using m.setMap(null) before rendering new results, ensuring the map remains clean and accurate during multiple searches.

## 3. AI-Assisted Components & Iterative Design
I utilized AI for non-core boilerplate and environment-specific tasks:

- **Iterative CSS Design (style.css)**: I used AI to research modern CSS styles and layouts. Through a trial-and-error approach, I experimented with different configurations suggested by the AI to achieve a responsive card-based layout that looked professional. 
- **Setup (setup.sh)**: I used AI to write the logic that identifies and terminates processes on Port 5000. This ensures the app runs reliably on different machines.
  
  - During development, I encountered a common macOS issue where Port 5000 is occupied by system services. I chose to use AI to find a reliable script-based solution for this, ensuring that the application remains robust and portable. This allows any reviewer to run the setup script on their own machine without having to manually troubleshoot port conflicts.
