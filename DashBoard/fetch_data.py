# 1.Business Logic & External Services
import requests
import datetime

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

if __name__ == "__main__":
    print("Fetching Bitcoin data for the last 31 days...")
    bitcoin_data = fetch_bitcoin_data()
    print(bitcoin_data)

    print("\nFetching Bitcoin data for the last 1 year...")
    bitcoin_data_year = fetch_bitcoin_data(365)
    print(bitcoin_data_year)
