import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained classification model
model = YOLO(os.path.join(BASE_DIR, "best.pt"))


def predict_disease(image_path):

    results = model(image_path)

    result = results[0]

    # Get highest probability class
    class_id = result.probs.top1
    confidence = float(result.probs.top1conf)

    disease = model.names[class_id]

    return {
        "disease": disease,
        "confidence": round(confidence * 100, 2)
    }