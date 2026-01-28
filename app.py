import os
import requests
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

@app.route('/')
def index():
    if not GOOGLE_API_KEY:
        # Return an error when no api key is provided.
        return "Error: GOOGLE_API_KEY not set in environment variables.", 500
    return render_template('index.html', google_api_key=GOOGLE_API_KEY)


@app.route('/api/nearby', methods=['GET'])
def nearby_search():
    address = request.args.get("address")
    place_type = request.args.get("type")
   
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_API_KEY}"
    geocode_results = requests.get(geocode_url).json()
    print("SIRAJ GOOGLE", GOOGLE_API_KEY)

    if geocode_results.get('status') == 'REQUEST_DENIED':
            return jsonify({
                "status": "error",
                "message": "The Google API key is incorrect or invalid. Please check Google API key."
            }), 401

   
    # Check if Google actually found the address
    if geocode_results.get('status') == 'ZERO_RESULTS' or not geocode_results.get('results'):
        return jsonify({
            "status": "error",
            "message": f"Could not find the location: {address}"
        }), 404
    
    location = geocode_results["results"][0]['geometry']['location']

    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    payload = {
        "location": f"{location['lat']},{location['lng']}",
        "radius": 2000,
        "type": place_type,
        "key": GOOGLE_API_KEY
    }
    
    places_data = requests.get(places_url, params=payload).json()
  
    return jsonify({
        "location": location,
        "results": places_data.get('results', [])
    })
  

if __name__ == '__main__':
   app.run(debug=True, port=5000)
