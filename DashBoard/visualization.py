# 4. Visualization
import matplotlib.pyplot as plt
import os
from fetch_data import fetch_bitcoin_data
from manipulate_data import manipulate_bitcoin_data

# Directory to save plots
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)  # Ensure directory exists

# Step 1 - Line Plot
def plot_line_chart(data, period="31 days"):
    """Plot and save a line chart for Bitcoin prices."""
    dates, prices = zip(*data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='b', label="Closing Price")

    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.title(f"LinePlot Bitcoin Closing Prices Over {period}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Save plot as image
    plt.savefig(os.path.join(PLOT_DIR, "line_plot.png"))
    print("✅ Line plot saved as 'plots/line_plot.png'")

    plt.show()

# Step 2 - Bar Chart
def plot_bar_chart(data, period="Last 7 days"):
    """Plot and save a bar chart for Bitcoin closing prices of a specific week."""
    dates, prices = zip(*data)

    plt.figure(figsize=(8, 5))
    plt.bar(dates, prices, color='green', label="Closing Price")

    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.title(f"BarChart Bitcoin Closing Prices for {period}")
    plt.xticks(rotation=45)
    plt.legend()

    # Save plot as image
    plt.savefig(os.path.join(PLOT_DIR, "bar_chart.png"))
    print("✅ Bar chart saved as 'plots/bar_chart.png'")

    plt.show()

if __name__ == "__main__":
    print("📊 Fetching & plotting Bitcoin price trends...")

    # Fetch full data (default 31 days)
    full_data = fetch_bitcoin_data()

    # Manipulate data to get first & last week
    first_week, last_week, cleaned_data = manipulate_bitcoin_data()

    # Line plot for entire period
    if cleaned_data:
        plot_line_chart(cleaned_data, "31 Days")

    # Bar plot for last 7 days
    if last_week:
        plot_bar_chart(last_week, "Last 7 Days")
