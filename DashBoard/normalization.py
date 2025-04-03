# 5. Data Normalization
import numpy as np
import matplotlib.pyplot as plt
from fetch_data import fetch_bitcoin_data
from manipulate_data import manipulate_bitcoin_data
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.dates as mdates
from datetime import datetime
import os

# Directory to save plots
PLOT_DIR = "plots-snip"
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

def plot_normalized_comparison(dates, original_prices, normalized_prices):
    """Compare original and normalized plots side by side."""

    # Convert dates to datetime objects
    formatted_dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]


    plt.figure(figsize=(12, 6))

    # Subplot 1: Original Prices
    plt.subplot(1, 2, 1)
    plt.plot(formatted_dates, original_prices, marker='o', linestyle='-', color='b', label="Original Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Original Prices")
    plt.grid(True)
    plt.legend()
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))
    plt.xticks(rotation=45)

# Subplot 2: Normalized Prices
    plt.subplot(1, 2, 2)
    plt.plot(formatted_dates, normalized_prices, marker='s', linestyle='--', color='r', label="Normalized Prices")
    plt.xlabel("Date")
    plt.ylabel("Scaled Price")
    plt.title("Normalized Prices")
    plt.grid(True)
    plt.legend()
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))
    plt.xticks(rotation=45)


    # Adjust layout
    plt.tight_layout()

    # Save the comparison plot
    plt.savefig(os.path.join(PLOT_DIR, "comparison_plot.png"))
    print("✅ Comparison plot saved as 'plots/comparison_plot.png'")

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
