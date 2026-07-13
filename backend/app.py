from flask import Flask, request, jsonify
from preprocess import predict_disease
import os
import json


app = Flask(__name__)

# -------------------------------
# Upload folder
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------------------
# Load recommendations
# -------------------------------
with open(os.path.join(BASE_DIR,"recommendation.json"), "r") as f:
    recommendations = json.load(f)

# -------------------------------
# Home Route
# -------------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "🌱 AgriVision AI Backend Running Successfully"
    })

# -------------------------------
# Prediction Route
# -------------------------------
@app.route("/upload", methods=["POST"])
def upload():

    try:

        if "image" not in request.files:
            return jsonify({
                "success": False,
                "error": "No image uploaded"
            }), 400


        image = request.files["image"]


        if image.filename == "":
            return jsonify({
                "success": False,
                "error": "Empty filename"
            }), 400



        filepath = os.path.join(
            UPLOAD_FOLDER,
            image.filename
        )

        image.save(filepath)


        print("Image saved:", filepath)



        # YOLO prediction
        prediction = predict_disease(filepath)

        print("Prediction:", prediction)



        disease = prediction["disease"]



        # Search recommendation
        recommendation = recommendations.get(
            disease,
            {}
        )


        final_recommendation = {

            "status": recommendation.get(
                "status",
                disease
            ),

            "severity": recommendation.get(
                "severity",
                "Unknown"
            ),

            "treatment": recommendation.get(
                "treatment",
                "No recommendation available."
            )

        }


        print("Recommendation:", final_recommendation)



        return jsonify({

            "success": True,

            "filename": image.filename,


            "prediction": {

                "disease": final_recommendation["status"],

                "confidence": prediction["confidence"]

            },


            "recommendation": final_recommendation

        })


    except Exception as e:

        import traceback

        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }),500
# -------------------------------
# Run Flask
# -------------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )