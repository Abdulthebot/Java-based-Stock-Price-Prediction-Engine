package com.example.stockpredictor.controller;

import com.example.stockpredictor.dto.PredictionRequest;
import com.example.stockpredictor.dto.PythonApiResponse;
import com.example.stockpredictor.service.PredictionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1")
public class PredictionController {

    private final PredictionService predictionService;

    @Autowired
    public PredictionController(PredictionService predictionService) {
        this.predictionService = predictionService;
    }

    @PostMapping("/predict-stock")
    public ResponseEntity<PythonApiResponse> predictStock(@RequestBody PredictionRequest request) {
        if (request.getSequence() == null || request.getSequence().size() != 60) {
            return ResponseEntity.badRequest().body(null); // Simple validation
        }
        PythonApiResponse response = predictionService.getStockPrediction(request);
        return ResponseEntity.ok(response);
    }
}
