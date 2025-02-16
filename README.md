# MSA-150 Stock Analysis Tool 📈

## Overview
MSA-150 is a powerful stock analysis tool that identifies promising technical patterns based on the 150-day moving average. The application analyzes stocks from major indices (NASDAQ 100, S&P 500) and ETFs daily, helping traders identify potential opportunities by monitoring specific technical criteria.

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
