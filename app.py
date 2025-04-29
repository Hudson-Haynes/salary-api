from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load('model.joblib')

@app.route('/')
def home():
    return 'API is running'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [list(data.values())]
    prediction = model.predict(features)
    return jsonify({'predicted_salary': prediction[0]})
