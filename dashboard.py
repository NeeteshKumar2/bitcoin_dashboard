import requests
import numpy as np
import matplotlib.pyplot as plt
import threading
import time
import datetime

import requests
import numpy as np
import matplotlib.pyplot as plt
import threading
import time
import datetime

# Updated API URL and fetch function
API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

def fetch_bitcoin_data(days=31):
    """Fetch Bitcoin historical data from CoinGecko API.

    Args:
        days (int): Number of days to fetch (default: 31).
    
    Returns:
        dict: A dictionary with dates as keys and closing prices as values.
    """
    params = {"vs_currency": "usd", "days": days}

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad response codes
        data = response.json()
        
        # Convert timestamps to human-readable dates
        prices = {datetime.datetime.utcfromtimestamp(item[0] / 1000).strftime('%Y-%m-%d'): item[1]
                  for item in data.get("prices", [])}
        return prices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

# The rest of the code remains the same for analysis, visualization, manipulation, etc.


# Function for data analysis
def analyze_data(data):
    prices = np.array(list(data.values()))
    mean_price = np.mean(prices)
    median_price = np.median(prices)
    std_dev_price = np.std(prices)
    
    print(f"Average Price: ${mean_price:.2f}")
    print(f"Median Price: ${median_price:.2f}")
    print(f"Standard Deviation: ${std_dev_price:.2f}")
    return prices

# Function for data manipulation
def manipulate_data(data):
    sorted_data = sorted(data.items())
    first_week_data = sorted_data[:7]
    last_week_data = sorted_data[-7:]
    
    print("First Week Data:", first_week_data)
    print("Last Week Data:", last_week_data)
    
    return first_week_data, last_week_data

def visualize_data(prices_dict, first_week_data, last_week_data):
    # Ensure prices_dict is a dictionary where keys are dates and values are prices
    if not isinstance(prices_dict, dict):
        print("Error: Expected a dictionary for prices_dict.")
        return
    
    # Extract dates and prices from the dictionary
    dates = list(prices_dict.keys())  # This should be a list of date strings
    prices = list(prices_dict.values())  # This should be a list of corresponding prices

    # Check if the dates and prices lists are non-empty
    if not dates or not prices:
        print("Error: No data to plot.")
        return
    
    # Line plot for the entire period
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, label='Closing Prices')
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.title("Bitcoin Closing Prices Over Time")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("bitcoin_prices.png")

    # Bar chart for the first week and last week
    first_week_dates = [date for date, _ in first_week_data]
    first_week_prices = [price for _, price in first_week_data]
    
    last_week_dates = [date for date, _ in last_week_data]
    last_week_prices = [price for _, price in last_week_data]
    
    plt.figure(figsize=(10, 5))
    plt.bar(first_week_dates, first_week_prices, color='blue', alpha=0.7, label="First Week")
    plt.bar(last_week_dates, last_week_prices, color='red', alpha=0.7, label="Last Week")
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.title("Bitcoin Prices: First Week vs Last Week")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("bitcoin_weekly_comparison.png")


# Function for data normalization
def normalize_data(prices):
    min_price = np.min(prices)
    max_price = np.max(prices)
    normalized_prices = (prices - min_price) / (max_price - min_price)
    
    print(f"Min Price: ${min_price:.2f}")
    print(f"Max Price: ${max_price:.2f}")
    
    plt.figure(figsize=(10, 5))
    plt.plot(prices, label="Original Data", color='blue')
    plt.plot(normalized_prices, label="Normalized Data", color='green')
    plt.title("Bitcoin Prices: Original vs Normalized")
    plt.legend()
    plt.tight_layout()
    plt.savefig("bitcoin_normalization_comparison.png")

# Function to simulate real-time updates using threading
def fetch_data_periodically(days=31):
    def fetch_and_update():
        while True:
            print("Fetching new data...")
            data = fetch_bitcoin_data(days)
            if data:
                print("Data fetched successfully.")
                analyze_data(data)
                first_week_data, last_week_data = manipulate_data(data)
                prices = np.array(list(data.values()))
                visualize_data(prices, first_week_data, last_week_data)
                normalize_data(prices)
            else:
                print("Failed to fetch data.")
            
            time.sleep(10)  # Simulate periodic updates every 10 seconds

    # Create and start a new thread
    update_thread = threading.Thread(target=fetch_and_update)
    update_thread.start()

def run_dashboard():
    # Fetch initial data (for 31 days)
    data = fetch_bitcoin_data(days=31)
    if data:
        print("Initial Data Fetched.")
        analyze_data(data)
        first_week_data, last_week_data = manipulate_data(data)
        
        # Pass the dictionary (data) to visualize_data
        visualize_data(data, first_week_data, last_week_data)
        
        prices = np.array(list(data.values()))  # For normalization and analysis
        normalize_data(prices)
    else:
        print("No data to process.")

    # Start the periodic update in the background
    fetch_data_periodically()


# Run the dashboard
if __name__ == "__main__":
    run_dashboard()
