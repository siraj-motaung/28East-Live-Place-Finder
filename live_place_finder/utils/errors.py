from flask import jsonify


def handle_geocode_errors(geocode_results: dict):
    status = geocode_results.get("status")

    if status == "REQUEST_DENIED":
        return jsonify({
            "status": "error",
            "message": "Invalid Google API key."
        }), 401

    if status == "ZERO_RESULTS" or not geocode_results.get("results"):
        return jsonify({
            "status": "error",
            "message": "Location not found."
        }), 404

    return None
