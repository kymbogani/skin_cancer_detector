# model_service.py
# Single Responsibility: only handles model loading and prediction

import pickle
import numpy as np
from tensorflow.keras.models import load_model
from config import Config


class ModelService:
    """
    Loads the trained model once and runs predictions.
    Open/Closed: extend by subclassing, not modifying.
    """

    def __init__(self):
        print("Loading model...")
        self._model = load_model(Config.MODEL_PATH, compile=False)
        print("Model loaded!")

        with open(Config.CLASSES_PATH, "rb") as f:
            self._classes = pickle.load(f)
        print("Classes:", self._classes)

    def predict(self, image_array: np.ndarray) -> dict:
        """
        Run prediction on preprocessed image array.
        Returns raw scores dict: { class_name: score_percent }
        """
        preds = self._model.predict(image_array, verbose=0)[0]

        all_scores = {
            self._classes[i]: round(float(preds[i]) * 100, 2)
            for i in range(len(self._classes))
        }

        best_idx   = int(np.argmax(preds))
        best_label = self._classes[best_idx]
        confidence = float(preds[best_idx])

        return {
            "label":      best_label,
            "confidence": confidence,
            "all_scores": all_scores
        }

    def build_response(self, prediction: dict) -> dict:
        """
        Build the full API response from raw prediction.
        Single Responsibility: mapping result → response shape.
        """
        label      = prediction["label"]
        confidence = prediction["confidence"]
        all_scores = prediction["all_scores"]

        # Low confidence → uncertain
        if confidence < Config.CONFIDENCE_MIN:
            response = dict(Config.UNCERTAIN_META)
            response["confidence"] = round(confidence * 100, 2)
            response["all_scores"] = all_scores
            return response

        meta = Config.CLASS_META.get(label, Config.CLASS_META["Benign"])

        return {
            "prediction": label,
            "confidence": round(confidence * 100, 2),
            "risk":       meta["risk"],
            "color":      meta["color"],
            "bg":         meta["bg"],
            "border":     meta["border"],
            "icon":       meta["icon"],
            "desc":       meta["desc"],
            "advice":     meta["advice"],
            "urgency":    meta["urgency"],
            "all_scores": all_scores,
            "disclaimer": "⚠️ This is NOT a medical diagnosis. Always consult a licensed dermatologist."
        }