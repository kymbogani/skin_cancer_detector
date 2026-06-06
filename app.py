# app.py — entry point only, thin as possible
import os
from flask import Flask
from flask_cors import CORS

from config import Config
from services.model_service import ModelService
from routes.predict_routes import predict_bp, init_routes


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = Config.MAX_CONTENT_LENGTH
    app.config["UPLOAD_FOLDER"]      = Config.UPLOAD_FOLDER

    CORS(app)

    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

    # Create and inject model service
    ms = ModelService()
    init_routes(ms)

    # Register blueprint
    app.register_blueprint(predict_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)