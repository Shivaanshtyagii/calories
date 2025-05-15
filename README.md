🏃‍♂️ Calories Burnt Prediction

This project predicts the number of calories burnt during physical activities based on biometric and exercise data. It's built using Python, Machine Learning (Scikit-learn), and served through a Flask API.

🚀 Live API: https://calories-2f7w.onrender.com

📌 Features

Predicts calories burnt using regression models.

Built with Flask and deployed on Render.

Lightweight and fast REST API for integration.

Trained on real-world exercise dataset.

📁 Project Structure
calories/
├── calories.csv              # Dataset
├── calories.pkl              # Trained model (Pickle format)
├── main.py                   # Flask API endpoint
├── model.py                  # Model training script
├── requirements.txt          # Dependencies

📊 Input Features

Gender (male / female)

Age (years)

Height (cm)

Weight (kg)

Duration (minutes)

Heart_Rate (bpm)

Body_Temp (°C)

🌐 API Usage

🔗 Endpoint
POST https://calories-2f7w.onrender.com/predict
🧾 Sample Request
{
  "Gender": "male",
  "Age": 25,
  "Height": 175,
  "Weight": 70,
  "Duration": 30,
  "Heart_Rate": 110,
  "Body_Temp": 37.5
}
✅ Sample Response
{
  "predicted_calories": 159.42
}
🛠️ Local Setup

To run the project locally:
git clone https://github.com/Shivaanshtyagii/calories.git
cd calories
pip install -r requirements.txt
python main.py
Then access the API at:http://127.0.0.1:5000/predict

🧠 Train Your Own Model

To retrain the ML model:

This will generate a new calories.pkl file used by the API.

🤛 Author

Shivansh Tyagi
🔗 GitHub: @Shivaanshtyagii🌍
API: https://calories-2f7w.onrender.com
