from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your model
model = pickle.load(open("rfr.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    try:
        Gender = data["Gender"]
        Age = data["Age"]
        Height = data["Height"]
        Weight = data["Weight"]
        Duration = data["Duration"]
        Heart_rate = data["Heart_rate"]
        Body_temp = data["Body_temp"]

        features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
        prediction = model.predict(features)

        return jsonify({"calories_burned": round(prediction[0], 2)})

    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
