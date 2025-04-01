from fetch_data import fetch_bitcoin_data

def manipulate_bitcoin_data(days=31):
    """Sort, slice, and clean Bitcoin historical price data.

    Args:
        days (int): Number of days to fetch (default: 31).

    Returns:
        tuple: First 7 days, Last 7 days, and Cleaned full dataset.
    """
    # Fetch data
    data = fetch_bitcoin_data(days)

    if not data:
        print("No data available for manipulation.")
        return None, None, None

    # Sort data by date (ascending order)
    sorted_data = sorted(data.items())  # List of tuples: [(date, price), (date, price), ...]

    # Slice first 7 days (early trends)
    first_week_data = sorted_data[:7]

    # Slice last 7 days (recent trends)
    last_week_data = sorted_data[-7:]

    # Clean data (remove missing or invalid values)
    cleaned_data = [(date, price) for date, price in sorted_data if price is not None]

    # Print sliced data
    print("\n📅 First 7 Days of Bitcoin Prices:")
    for date, price in first_week_data:
        print(f"{date}: ${price:.2f}")

    print("\n📅 Last 7 Days of Bitcoin Prices:")
    for date, price in last_week_data:
        print(f"{date}: ${price:.2f}")

    return first_week_data, last_week_data, cleaned_data

if __name__ == "__main__":
    print("🔄 Manipulating Bitcoin price data for the last 31 days...\n")
    manipulate_bitcoin_data(31)

    print("\n🔄 Manipulating Bitcoin price data for the last 1 year...\n")
    manipulate_bitcoin_data(365)
