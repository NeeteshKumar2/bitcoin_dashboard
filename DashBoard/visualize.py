import matplotlib.pyplot as plt
from fetch_data import fetch_bitcoin_data

def visualize_data(data):
    """Plot Bitcoin closing prices over time."""
    if not data:
        print("No data available for visualization.")
        return
    
    dates = list(data.keys())
    prices = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker="o", linestyle="-", color="b", label="Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Bitcoin Price Trend")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    bitcoin_data = fetch_bitcoin_data()
    visualize_data(bitcoin_data)
