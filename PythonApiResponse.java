package com.example.stockpredictor.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
public class PythonApiResponse {
    @JsonProperty("predicted_price")
    private Double predictedPrice;
}
