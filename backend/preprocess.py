import cv2
from ultralytics import YOLO

# Load trained model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = YOLO(os.path.join(BASE_DIR, "best.pt"))


def predict_disease(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return {
            "disease": "Invalid Image",
            "confidence": 0
        }

    # Lower confidence threshold slightly
    results = model(image, conf=0.25)

    for result in results:

        if len(result.boxes) > 0:

            # Select the box with the highest confidence
            best_box = max(result.boxes, key=lambda x: float(x.conf))

            cls = int(best_box.cls.item())
            confidence = float(best_box.conf.item())

            disease = model.names[cls]

            return {
                "disease": disease,
                "confidence": round(confidence * 100, 2)
            }

    # No disease detected by the model
    return {
        "disease": "Unknown",
        "confidence": 0
    }