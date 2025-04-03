import numpy as np
import matplotlib.pyplot as plt
import threading
import time
from fetch_data import fetch_bitcoin_data
from manipulate_data import manipulate_bitcoin_data
from visualization import plot_line_chart, plot_bar_chart
from normalization import min_max_scaling, plot_normalized_comparison

# Shared dictionary to store fetched data
aggregated_data = {}

# Lock for thread-safe access
data_lock = threading.Lock()

def fetch_and_store_data(days, label):
    """Fetch Bitcoin data for a given period and store it in shared storage."""
    while True:
        print(f"🌍 Fetching {label} data...")
        data = fetch_bitcoin_data(days)

        if data:
            print(f"✅ {label} Data fetched successfully.")
            sorted_data = sorted(data.items())  # Sort data by date

            with data_lock:  # Lock to prevent race conditions
                aggregated_data[label] = sorted_data

            visualize_and_analyze_data()

        else:
            print(f"❌ Failed to fetch {label} data.")

        print(f"⏳ Waiting before next fetch for {label}...")
        time.sleep(10)  # Adjust fetch interval

def visualize_and_analyze_data():
    """Aggregates, visualizes, normalizes, and compares fetched data."""
    with data_lock:  # Ensure thread-safe access
        if not aggregated_data:
            return  # No data to display yet

        # Merge all available data
        merged_data = []
        for label, data in aggregated_data.items():
            merged_data.extend(data)

        merged_data = sorted(merged_data)  # Ensure chronological order
        dates, prices = zip(*merged_data)

        # Convert to NumPy array
        prices_array = np.array(prices)

        # Plot visualizations
       # plot_line_chart(merged_data, "Aggregated Data")
        #plot_bar_chart(merged_data[-7:], "Last 7 Days")

        # Normalize prices
        normalized_prices, min_price, max_price = min_max_scaling(prices_array)

        # Plot normalized vs original comparison
        plot_normalized_comparison(dates, prices_array, normalized_prices)

def start_threads():
    """Start multiple threads to fetch data concurrently."""
    threads = []

    # Create Thread 1: Fetch 31 days of data
    t1 = threading.Thread(target=fetch_and_store_data, args=(31, "31 Days"), daemon=True)
    threads.append(t1)

    # Create Thread 2: Fetch 365 days of data
    t2 = threading.Thread(target=fetch_and_store_data, args=(365, "1 Year"), daemon=True)
    threads.append(t2)

    # Start both threads
    for t in threads:
        t.start()

if __name__ == "__main__":
    print("🚀 Starting concurrent Bitcoin data fetching...")
    start_threads()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🔴 Stopping all threads.")
