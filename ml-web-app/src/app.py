from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the machine learning model
with open('../model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get user input from the form
        user_input = request.form.to_dict()
        # Convert input to the format expected by the model
        input_data = np.array([[float(user_input['feature1']), float(user_input['feature2']), 
                                 float(user_input['feature3'])]])  # Adjust based on your model's input features
        # Make prediction
        prediction = model.predict(input_data)[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)