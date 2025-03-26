from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open('crop_yield_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load sample feature names from training data
feature_columns = ['Year', 'Area', 'Rainfall', 'Temperature', 'Humidity', 'Price', 
                   'Location_Gulbarga', 'Location_Hassan', 'Location_Kasaragodu', 
                   'Location_Kodagu', 'Location_Madikeri', 'Location_Mangalore', 
                   'Location_Mysuru', 'Location_Raichur', 'Soil type_Arid and Desert', 
                   'Soil type_Black', 'Soil type_Black cotton', 'Soil type_Clay', 
                   'Soil type_Clay loam', 'Soil type_Drained loam', 'Soil type_Dry sandy', 
                   'Soil type_Gravelly sand', 'Soil type_Heavy clay', 'Soil type_Heavy cotton', 
                   'Soil type_Laterite', 'Soil type_Light sandy', 'Soil type_Loam', 
                   'Soil type_Medium textured', 'Soil type_Medium textured clay', 
                   'Soil type_Red', 'Soil type_Red laterite', 'Soil type_River basins', 
                   'Soil type_Sandy', 'Soil type_Sandy loam', 'Soil type_Teelah', 
                   'Soil type_Well drained', 'Soil type_loamy sand', 'Irrigation_Drip', 
                   'Irrigation_Spray', 'Crops_Blackgram', 'Crops_Cardamum', 'Crops_Cashew', 
                   'Crops_Cocoa', 'Crops_Coconut', 'Crops_Coffee', 'Crops_Cotton', 
                   'Crops_Ginger', 'Crops_Groundnut', 'Crops_Paddy', 'Crops_Pepper', 
                   'Crops_Tea', 'Season_Rabi', 'Season_Zaid']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input
        data = request.json
        print("Received data:", data)

        # Convert input to DataFrame
        df = pd.DataFrame([data])

        # Add missing columns with default values (0)
        for col in feature_columns:
            if col not in df.columns:
                df[col] = 0  # Default to 0 for missing categorical data

        # Reorder columns to match model input order
        df = df[feature_columns]
        print("Processed DataFrame:", df)

        # Make prediction
        prediction = model.predict(df)[0]

        return jsonify({'prediction': float(prediction*15000)})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)