import numpy as np
import pandas as pd

def generate_data():
    """Generates synthetic stock price data and saves it to a CSV file."""
    # Generate a sine wave with some noise
    time = np.arange(0, 500, 0.1)
    amplitude = np.sin(time) + np.random.normal(scale=0.1, size=len(time))
    
    # Create a baseline price and add the wave to it
    baseline_price = 100
    price = baseline_price + amplitude * 10
    
    df = pd.DataFrame({'Price': price})
    df.to_csv('synthetic_stock_data.csv', index=False)
    
    print("Synthetic stock data 'synthetic_stock_data.csv' created successfully.")
    print(f"Generated {len(df)} data points.")

if __name__ == '__main__':
    generate_data()
