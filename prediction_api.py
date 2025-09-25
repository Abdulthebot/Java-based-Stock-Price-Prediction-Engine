from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import joblib

app = Flask(__name__)

# Load the trained model and scaler
try:
    model = tf.keras.models.load_model('models/lstm_stock_predictor.keras')
    scaler = joblib.load('models/scaler.pkl')
    print("Model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not scaler:
        return jsonify({'error': 'Model or scaler not loaded'}), 500

    try:
        data = request.get_json(force=True)
        # The API expects a list of 60 recent prices
        sequence = data['sequence']
        
        if len(sequence) != 60:
            return jsonify({'error': 'Input sequence must contain 60 timesteps'}), 400

        # Reshape, scale, and make prediction
        sequence_np = np.array(sequence).reshape(-1, 1)
        scaled_sequence = scaler.transform(sequence_np)
        input_data = np.reshape(scaled_sequence, (1, 60, 1))
        
        predicted_price_scaled = model.predict(input_data)
        
        # Inverse transform the prediction to get the actual price value
        predicted_price = scaler.inverse_transform(predicted_price_scaled)
        
        return jsonify({'predicted_price': float(predicted_price[0][0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Running on a different port than the first project
