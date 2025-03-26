# ml-web-app

This project is a web application that demonstrates predictions from a machine learning model using Flask. The application allows users to input data and receive predictions based on a pre-trained model.

## Project Structure

```
ml-web-app
├── src
│   ├── app.py            # Main application file
│   ├── static
│   │   └── style.css     # CSS styles for the web application
│   └── templates
│       └── index.html    # HTML template for user input and predictions
├── model
│   └── model.pkl         # Serialized machine learning model
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ml-web-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the `src` directory:
   ```
   cd src
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Enter the required input data in the form provided on the homepage.
- Click the submit button to receive predictions from the machine learning model.

## License

This project is licensed under the MIT License - see the LICENSE file for details.