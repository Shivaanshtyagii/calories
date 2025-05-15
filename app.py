import os
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("rfr.pkl", "rb"))

# Root route for basic check
@app.route("/", methods=["GET"])
def home():
    return "Calories Prediction API is live. Use POST /predict with JSON data."

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    try:
        # Extract input features from request
        Gender = data["Gender"]
        Age = data["Age"]
        Height = data["Height"]
        Weight = data["Weight"]
        Duration = data["Duration"]
        Heart_rate = data["Heart_rate"]
        Body_temp = data["Body_temp"]

        # Convert input to NumPy array for prediction
        features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
        prediction = model.predict(features)

        # Return prediction result
        return jsonify({"calories_burned": round(prediction[0], 2)})

    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
