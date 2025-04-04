# Bitcoin Price Dashboard

## Overview
This project is a Python-based dashboard that fetches, analyzes, manipulates, visualizes, and normalizes historical Bitcoin price data from the CoinGecko API. It also includes a simulated real-time data streaming feature using threading.

## Features
- **Fetch Data**: Retrieve historical Bitcoin price data from the CoinGecko API.
- **Data Analysis**: Compute statistical metrics like mean, median, and standard deviation using NumPy.
- **Data Manipulation**: Sort, slice, and clean Bitcoin price data, extracting the first and last 7 days for trend analysis.
- **Visualization**: Generate line and bar charts using Matplotlib.
- **Normalization**: Apply Min-Max normalization to compare raw and scaled price data.
- **Simulated Data Streaming**: Fetch and update Bitcoin price data in real-time using threading for concurrency.

## Project Structure
```
├── fetch_data.py         # Fetches Bitcoin data from CoinGecko API
├── process_data.py       # Performs statistical analysis
├── manipulate_data.py    # Sorts, slices, and cleans data
├── visualization.py      # Generates line and bar charts
├── normalization.py      # Normalizes and compares price data
├── datastream.py     # Implements real-time data streaming with threading
├── plots-snip/           # Directory for saving generated plots
├── README.md             # Project documentation
├── requirements.txt      # Required Python packages
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/neeteshkahar2/bitcoin-dashboard.git
   cd bitcoin-dashboard
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Fetching Bitcoin Data:**
   ```sh
   python fetch_data.py
   ```
2. **Analyzing Bitcoin Price Trends:**
   ```sh
   python analyze_data.py
   ```
3. **Manipulating Data for Trends:**
   ```sh
   python manipulate_data.py
   ```
4. **Visualizing Bitcoin Price Trends:**
   ```sh
   python visualization.py
   ```
5. **Normalizing Bitcoin Prices:**
   ```sh
   python normalization.py
   ```
6. **Simulated Data Streaming (Concurrent Fetching):**
   ```sh
   python data_streaming.py
   ```

## Requirements
See `requirements.txt` for a list of required dependencies.

## License
This project is open-source and free to use. Modify and distribute as needed.

## Author
Developed by [Neetesh Kumar](https://github.com/NeeteshKumar2)

