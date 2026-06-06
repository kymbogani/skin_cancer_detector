# image_service.py
# Single Responsibility: only handles image loading and preprocessing

import numpy as np
from PIL import Image
from config import Config


class ImageService:
    """Handles all image preprocessing. Nothing else."""

    @staticmethod
    def allowed_file(filename: str) -> bool:
        return (
            "." in filename and
            filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXT
        )

    @staticmethod
    def preprocess(image_path: str) -> np.ndarray:
        """
        Load image from path, resize to model input size,
        return as numpy array ready for prediction.
        EfficientNet handles its own pixel scaling internally.
        """
        img = Image.open(image_path).convert("RGB")
        img = img.resize((Config.IMG_SIZE, Config.IMG_SIZE))
        arr = np.array(img, dtype=np.float32)
        return np.expand_dims(arr, axis=0)   # shape: (1, 300, 300, 3)