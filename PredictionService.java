package com.example.stockpredictor.service;

import com.example.stockpredictor.dto.PredictionRequest;
import com.example.stockpredictor.dto.PythonApiResponse;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PredictionService {

    private final RestTemplate restTemplate = new RestTemplate();
    
    // The URL of the Python Flask API
    private final String pythonApiUrl = "http://127.0.0.1:5001/predict";

    public PythonApiResponse getStockPrediction(PredictionRequest request) {
        // Make a POST request to the Python API and get the response
        return restTemplate.postForObject(pythonApiUrl, request, PythonApiResponse.class);
    }
}
