from flask import Flask
from flask_cors import CORS

from live_place_finder.config import Config
from live_place_finder.services.google_maps_service import GoogleMapsService
from live_place_finder.routes.places import places_bp, init_places
from live_place_finder.routes.users import users_bp


def create_app():
    app = Flask(__name__)
    CORS(app)


    Config.setup_logging()

    # Initialise service (Dependency Injection)
    try:
        google_service = GoogleMapsService(Config.GOOGLE_API_KEY)
    except ValueError:
        google_service = None

    # Inject dependencies into routes
    init_places(google_service, Config)

    # Register blueprint
    app.register_blueprint(places_bp)
    app.register_blueprint(users_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)