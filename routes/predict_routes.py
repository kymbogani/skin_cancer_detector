# predict_routes.py
# Single Responsibility: only handles HTTP routing

import os
from flask import Blueprint, request, jsonify, render_template
from werkzeug.utils import secure_filename

from config import Config
from services.image_service import ImageService
from services.model_service import ModelService

# Blueprint — Open/Closed: routes are isolated and extendable
predict_bp = Blueprint("predict", __name__)

# Dependency Injection — pass model_service in from app.py
model_service  = None
image_service  = ImageService()


def init_routes(ms: ModelService):
    """Inject the ModelService dependency."""
    global model_service
    model_service = ms


@predict_bp.route("/")
def index():
    return render_template("index.html")


@predict_bp.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]

    if not file or file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    if not image_service.allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Use JPG, PNG, or WEBP."}), 400

    try:
        filename  = secure_filename(file.filename)
        save_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(save_path)

        # Step 1: preprocess
        arr = image_service.preprocess(save_path)

        # Step 2: predict
        raw = model_service.predict(arr)

        # Step 3: build response
        response = model_service.build_response(raw)

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@predict_bp.route("/health")
def health():
    return jsonify({"status": "ok"})