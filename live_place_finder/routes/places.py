from flask import Blueprint, request, jsonify, render_template


from live_place_finder.utils.errors import handle_geocode_errors


places_bp = Blueprint("places", __name__)

google_service = None
config = None


def init_places(service, app_config):
    global google_service, config
    google_service = service
    config = app_config


@places_bp.route("/")
def index():
    if not config.GOOGLE_API_KEY:
        return "Error: GOOGLE_API_KEY not set in environment variables.", 500

    return render_template("index.html", google_api_key=config.GOOGLE_API_KEY)


@places_bp.route("/api/nearby", methods=["GET"])
def nearby_search():
    if not google_service:
        return jsonify({
            "status": "error",
            "message": "Service not initialized"
        }), 500

    address = request.args.get("address")
    place_type = request.args.get("type")

    geocode_results = google_service.geocode(address)

    error_response = handle_geocode_errors(geocode_results)
    if error_response:
        return error_response

    location = geocode_results["results"][0]["geometry"]["location"]

    places_data = google_service.nearby_search(
        location["lat"],
        location["lng"],
        place_type
    )

    return jsonify({
        "location": location,
        "results": places_data.get("results", [])
    })
