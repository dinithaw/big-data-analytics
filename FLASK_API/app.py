from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open('crop_yield_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

# Define the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get data from the frontend (JSON)
    
    # Convert data into a DataFrame
    df = pd.DataFrame([data])
    
    # Ensure it matches the model's expected format
    prediction = model.predict(df)[0]  # Get the predicted value

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)