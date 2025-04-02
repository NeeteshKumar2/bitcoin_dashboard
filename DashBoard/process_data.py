# 2. Data Analysis
import numpy as np
from fetch_data import fetch_bitcoin_data

def analyze_bitcoin_data(days=31):
    """Analyze Bitcoin historical price data using NumPy.

    Args:
        days (int): Number of days to fetch (default: 31).

    Returns:
        tuple: Mean, Median, and Standard Deviation of prices.
    """
    # Fetch data
    data = fetch_bitcoin_data(days)
    
    if not data:
        print("No data available for analysis.")
        return None, None, None
    
    # Step 1 - Convert prices to NumPy array
    prices = np.array(list(data.values()))
    
    # Step 2 - Compute statistics
    mean_price = np.mean(prices)
    median_price = np.median(prices)
    std_dev = np.std(prices)
    
    # Step 3 - Print results
    print(f"\n📊 Bitcoin Price Analysis for the Last {days} Days")
    print(f"📈 Average Price: ${mean_price:.2f}")
    print(f"📉 Median Price: ${median_price:.2f}")
    print(f"📊 Standard Deviation (Volatility): ${std_dev:.2f}")
    
    return mean_price, median_price, std_dev

if __name__ == "__main__":
    print("🔍 Analyzing Bitcoin price for the last 31(default) days...")
    analyze_bitcoin_data(31)

    '''print("\n🔍 Analyzing Bitcoin price for the last 1 year...")
    analyze_bitcoin_data(365)'''
