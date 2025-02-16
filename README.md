# MSA-150 Stock Analysis Tool 📈

## Overview
MSA-150 is a powerful stock analysis tool that identifies promising technical patterns based on the 150-day moving average. The application analyzes stocks from major indices (NASDAQ 100, S&P 500) and ETFs daily, helping traders identify potential opportunities by monitoring specific technical criteria.

## Features
* Stock Data Fetching:
- The script fetches historical stock price data for the past year using the Yahoo Finance API via the yfinance library.

* Key Calculations:
- Calculates the 50-day, 150-day, and 200-day Simple Moving Averages (SMAs) for each stock.
- Identifies stocks that:
    Are within 5% of their 150-day SMA.
    Have a rising 150-day SMA (i.e., steadily increasing over the last 10 days).
    Exhibit "Golden Cross" (50-day SMA crossing above 200-day SMA) or "Red Cross" (50-day SMA crossing below 200-day SMA)       patterns in the last 10 days.

* Result Formatting:
- Outputs the results in a structured DataFrame format for further analysis or display.

## Usage
### Input

The script processes a predefined list of stock tickers:
tickers = ["ADBE", "AMD", "ABNB", "GOOGL", "GOOG", "AMZN", "AEP", "AMGN", "ADI", "ANSS",...]
You can customize this list by adding or removing stock tickers.

### Output

The script returns a table with stocks meeting specific criteria:
- The stock ticker.
- A label indicating its condition:
    - Gold Stock: Indicates a "Golden Cross."
    - Red Stock: Indicates a "Red Cross."


## Code Details

### Main Functionality

* Data Fetching:
- Historical stock data is fetched using yfinance for the past year to ensure sufficient data for SMA calculations.

* SMA Calculation:
- Three SMAs are calculated:
    SMA_50: 50-day SMA.
    SMA_150: 150-day SMA.
    SMA_200: 200-day SMA.
- Missing values (NaN) in the SMAs are handled using forward and backward filling (ffill and bfill).

* Condition Checks:
- Range Check: Stocks within 5% of the 150-day SMA.
- Rising SMA: The 150-day SMA is steadily increasing.
- Golden/Red Cross:
    - Golden Cross: SMA_50 crosses above SMA_200.
    - Red Cross: SMA_50 crosses below SMA_200.

* Output:
Results are stored in a DataFrame and displayed as a formatted table.

## Limitations
- Incomplete Data:
    If a stock lacks sufficient historical data, it is skipped.
- Hardcoded Tickers:
    The list of tickers is static and must be manually updated in the script.
- Processing Time:
    Analyzing a large number of tickers may take significant time due to API calls.


Potential Enhancements
Dynamic Ticker Input:
Allow users to input tickers via a file or command line.
Enhanced Analysis:
Add more technical indicators, such as RSI or MACD.
Visualization:
Provide graphical outputs, such as price charts with SMA overlays.

## Features
- **Daily Analysis**: Automatic refresh at midnight to ensure up-to-date data
- **Multiple Markets**: Covers NASDAQ 100, S&P 500, additional stocks, and ETFs
- **Technical Indicators**: 
  - Stocks within 5% above their 150-day moving average
  - Upward trend confirmation
  - Special "Gold" and "Red" stock status indicators
- **User-Friendly Interface**: Clean, intuitive design with detailed stock information

## Technical Requirements
- Python 3.8+
- Required packages:
  ```
  streamlit==1.31.0
  pandas==2.1.4
  yfinance==0.2.36
  tabulate==0.9.0
  ```

## Installation & Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/msa-150.git
   cd msa-150
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Access the application through your web browser
2. Wait for the daily reset at midnight
3. Click the "Analyze Stocks" button to fetch current data
4. Browse different market segments through the tabs
5. View detailed information about stocks meeting the technical criteria

## Data Sources
- Stock data is fetched from Yahoo Finance using the yfinance library
- All technical calculations are performed in real-time

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License
MIT License - feel free to use this project as you wish!

## Contact
Harel Hanuka
- GitHub: [[@yourusername](https://github.com/HYMH92
)]
- LinkedIn: [[Your LinkedIn Profile](https://www.linkedin.com/in/harel-hanuka/
)]
