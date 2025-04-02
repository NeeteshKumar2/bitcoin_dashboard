# 5. Data Normalization
import numpy as np
import matplotlib.pyplot as plt
from fetch_data import fetch_bitcoin_data
from manipulate_data import manipulate_bitcoin_data
import os

# Directory to save plots
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)  # Ensure directory exists

# Step 1- Normalization Technique:
def min_max_scaling(prices):
    """Apply Min-Max normalization to scale prices between 0 and 1."""
    min_value = np.min(prices)
    max_value = np.max(prices)
    
    normalized_prices = (prices - min_value) / (max_value - min_value)
    
    print(f"📌 Min Price: {min_value:.2f}, Max Price: {max_value:.2f}")
    print(f"📌 Normalization Price: {normalized_prices}")
    return normalized_prices, min_value, max_value

# Step 2 - Comparison Plot:
def plot_normalized_comparison(dates, original_prices, normalized_prices):
    """Plot original vs. normalized prices on the same graph."""
    plt.figure(figsize=(10, 5))

    # Original Data
    plt.plot(dates, original_prices, marker='o', linestyle='-', color='b', label="Original Prices")

    # Normalized Data
    plt.plot(dates, normalized_prices, marker='s', linestyle='--', color='r', label="Normalized Prices")

    plt.xlabel("Date")
    plt.ylabel("Price (Scaled / USD)")
    plt.title("Bitcoin Prices: Raw vs. Normalized")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Save the plot
    plt.savefig(os.path.join(PLOT_DIR, "normalized_comparison.png"))
    print("✅ Normalized comparison plot saved as 'plots/normalized_comparison.png'")

    plt.show()

if __name__ == "__main__":
    print("📊 Fetching & Normalizing Bitcoin price data...")

    # Fetch Bitcoin data
    bitcoin_data = fetch_bitcoin_data()

    # Convert data to sorted list
    sorted_data = sorted(bitcoin_data.items())  # Sorted by date
    dates, prices = zip(*sorted_data)

    # Convert prices to NumPy array
    prices_array = np.array(prices)

    # Normalize prices
    normalized_prices, min_price, max_price = min_max_scaling(prices_array)

    # Plot original vs. normalized comparison
    plot_normalized_comparison(dates, prices_array, normalized_prices)
