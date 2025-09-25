# Hybrid Stock Prediction Engine (Java + Python)

This project demonstrates a hybrid system architecture, integrating a robust Java Spring Boot backend with a specialized Python AI service for stock price prediction. It showcases the ability to bridge enterprise-grade applications with modern machine learning capabilities. [cite_start]The LSTM model backend was built in Python, achieving a 12% higher accuracy than baseline models[cite: 29].

## Architecture
- **Java Spring Boot Backend:** The main application that exposes a public API for clients.
- **Python Flask AI Service:** A microservice that loads a pre-trained TensorFlow LSTM model and serves predictions over a REST API.

## How to Run the System

### 1. The Python AI Service
First, set up and run the Python service.
```bash
# Navigate to the Python service directory
cd python-prediction-service

# Install dependencies
pip install -r requirements.txt

# Step 1: Generate synthetic stock data
python generate_stock_data.py

# Step 2: Run the Jupyter Notebook 'stock_prediction_model.ipynb'
# This trains and saves the LSTM model and the data scaler.

# Step 3: Start the Python Flask API
# It will run on [http://127.0.0.1:5001](http://127.0.0.1:5001)
python prediction_api.py
```

### 2. The Java Spring Boot Backend
With the Python service running, you can now start the Java application.
```bash
# Navigate to the Java backend directory
cd java-spring-boot-backend

# Build and run the Spring Boot application using Maven
./mvnw spring-boot:run
```
The Java service will run on `http://localhost:8080`.

### 3. Testing the Full System
Send a POST request to the **Java API**. It will, in turn, call the Python API and return the prediction.

```bash
curl -X POST http://localhost:8080/api/v1/predict-stock \
-H "Content-Type: application/json" \
-d '{
    "sequence": [
        100.1, 100.2, 100.3, 100.4, 100.5, 100.6, 100.7, 100.8, 100.9, 101.0,
        101.1, 101.2, 101.3, 101.4, 101.5, 101.6, 101.7, 101.8, 101.9, 102.0,
        102.1, 102.2, 102.3, 102.4, 102.5, 102.6, 102.7, 102.8, 102.9, 103.0,
        103.1, 103.2, 103.3, 103.4, 103.5, 103.6, 103.7, 103.8, 103.9, 104.0,
        104.1, 104.2, 104.3, 104.4, 104.5, 104.6, 104.7, 104.8, 104.9, 105.0,
        105.1, 105.2, 105.3, 105.4, 105.5, 105.6, 105.7, 105.8, 105.9, 106.0
    ]
}'
```

## Architect's Notes
The hybrid, microservice-based architecture was a deliberate choice. It allows for the separation of concerns: the Java backend can scale independently and handle complex business logic, while the Python service can be updated, retrained, and scaled specifically for its AI task. This modularity is a cornerstone of modern software design.
