from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load('./notebook/diamond_model.pkl')
scaler = joblib.load('./notebook/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        carat = float(request.form['carat'])
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        cut = int(request.form['cut'])
        color = int(request.form['color'])
        clarity = int(request.form['clarity'])

        features = np.array([[carat, depth, table, x, y, z, cut, color, clarity]])
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        return render_template('index.html', prediction_text=f"💎 Estimated Diamond Price: ${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"❌ Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
