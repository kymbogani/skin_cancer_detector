# config.py — Single Responsibility: all app settings here
import os

class Config:
    # Paths
    BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH    = os.path.join(BASE_DIR, "model", "skin_cancer_model.keras")
    CLASSES_PATH  = os.path.join(BASE_DIR, "model", "label_classes.pkl")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    # Model settings
    IMG_SIZE       = 300
    CONFIDENCE_MIN = 0.45

    # Flask settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXT        = {"png", "jpg", "jpeg", "webp", "bmp"}

    # Class metadata
    CLASS_META = {
        "Normal": {
            "risk":    "No Risk",
            "color":   "#2563eb",
            "bg":      "#eff6ff",
            "border":  "#bfdbfe",
            "icon":    "✓",
            "desc":    "Your skin appears healthy with no visible abnormalities detected.",
            "advice":  "Continue regular self-examinations and wear sunscreen daily (SPF 30+).",
            "urgency": "No Action Needed"
        },
        "Benign": {
            "risk":    "Low Risk",
            "color":   "#059669",
            "bg":      "#ecfdf5",
            "border":  "#a7f3d0",
            "icon":    "◉",
            "desc":    "A non-cancerous growth was detected. Generally not dangerous.",
            "advice":  "Schedule a routine dermatology check annually to monitor for changes.",
            "urgency": "Routine Monitoring"
        },
        "Premalignant": {
            "risk":    "Medium Risk",
            "color":   "#d97706",
            "bg":      "#fffbeb",
            "border":  "#fde68a",
            "icon":    "⚠",
            "desc":    "The lesion shows early warning signs that may develop into cancer.",
            "advice":  "Please consult a dermatologist within the next 2–4 weeks.",
            "urgency": "See Doctor Soon"
        },
        "Malignant": {
            "risk":    "High Risk",
            "color":   "#dc2626",
            "bg":      "#fef2f2",
            "border":  "#fecaca",
            "icon":    "!",
            "desc":    "The lesion shows characteristics associated with skin cancer.",
            "advice":  "Please seek immediate medical attention from a dermatologist.",
            "urgency": "Urgent — See Doctor Now"
        }
    }

    UNCERTAIN_META = {
        "prediction": "Uncertain",
        "risk":    "Unknown",
        "color":   "#6b7280",
        "bg":      "#f9fafb",
        "border":  "#e5e7eb",
        "icon":    "?",
        "desc":    "Image quality may be too low or the lesion is unclear.",
        "advice":  "Retake the photo in better lighting, close to the skin area.",
        "urgency": "Retake Photo",
        "disclaimer": "This is NOT a medical diagnosis. Always consult a dermatologist."
    }