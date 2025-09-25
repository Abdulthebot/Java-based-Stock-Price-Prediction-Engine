package com.example.stockpredictor.dto;

import lombok.Data;
import java.util.List;

@Data // Lombok annotation for getters, setters, etc.
public class PredictionRequest {
    private List<Double> sequence;
}
