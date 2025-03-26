# Crop Yield Prediction Web Application

This project demonstrates a machine learning model for predicting crop yields based on various features such as area, rainfall, temperature, soil type, and more. The model is deployed as a web application using Flask, allowing users to input data and receive predictions.

---

## Overview

The goal of this project is to predict crop yields based on various environmental and agricultural factors. The machine learning model was trained using a dataset containing features such as:
- Year
- Area
- Rainfall
- Temperature
- Humidity
- Soil type
- Irrigation method
- Crop type
- Season

The trained model is deployed as a Flask web application, where users can input data and receive predictions.

---

## Features

- **Machine Learning Model**: Uses an XGBoost regressor for crop yield prediction.
- **Web Interface**: A simple and user-friendly web interface for inputting data and viewing predictions.
- **REST API**: Exposes an API endpoint for programmatic access to predictions.
- **Model Persistence**: The trained model is saved as a pickle file for reuse.

---

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework for building the application.
- **XGBoost**: Machine learning library for training the model.
- **Pandas & NumPy**: Data manipulation and numerical computations.
- **Scikit-learn**: For preprocessing and evaluation metrics.
- **HTML/CSS**: For the web interface.
- **Pickle**: For saving and loading the trained model.

---