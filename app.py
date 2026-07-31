from flask import Flask
from flask_cors import CORS

from config import Config
from services.google_maps_service import GoogleMapsService
from routes.places import places_bp, init_places


def create_app():
    app = Flask(__name__)
    CORS(app)

    config = Config()

    # Initialise service (Dependency Injection)
    try:
        google_service = GoogleMapsService(config.GOOGLE_API_KEY)
    except ValueError:
        google_service = None

    # Inject dependencies into routes
    init_places(google_service, config)

    # Register blueprint
    app.register_blueprint(places_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)