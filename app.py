from flask import Flask, request, render_template
import joblib
import pandas as pd
app = Flask(__name__, template_folder='template')
model = joblib.load('rainfall_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [features]
    prediction = model.predict(final_features)
    output = 'Rain' if prediction[0] == 1 else 'No Rain'
    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)