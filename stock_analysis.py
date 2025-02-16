import requests
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from tabulate import tabulate


NSDK100 = [
    "ADBE", "AMD", "ABNB", "GOOGL", "GOOG", "AMZN", "AEP", "AMGN", "ADI", "ANSS",
    "AAPL", "AMAT", "APP", "ARM", "ASML", "AZN", "TEAM", "ADSK", "ADP", "AXON",
    "BKR", "BIIB", "BKNG", "AVGO", "CDNS", "CDW", "CHTR", "CHKP", "CTAS", "CSCO",
    "CTSH", "CMCSA", "CEG", "CPRT", "COST", "CRWD", "DDOG", "DXCM", "DOCU", "DLTR",
    "EA", "ENPH", "EXC", "EXPE", "FAST", "FTNT", "GILD", "HON", "ILMN", "INTC",
    "INTU", "ISRG", "JD", "KDP", "KLAC", "LRCX", "LCID", "LULU", "MRVL", "MTCH",
    "META", "MCHP", "MU", "MSFT", "MRNA", "MDLZ", "NTES", "NFLX", "NVDA", "NXPI",
    "OKTA", "ODFL", "ON", "ORLY", "PANW", "PAYX", "PYPL", "PDD", "PEP", "QCOM",
    "REGN", "ROP", "ROST", "SBUX", "SNPS", "TTWO", "TMUS", "TSLA", "TXN", "TTD",
    "VRSK", "VRTX", "WBD", "WDAY", "XEL", "ZS"
    ]

SP500 = [
    'MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD',
    'ABNB', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO',
    'AMZN', 'AMCR', 'AEE', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'AME', 'AMGN',
    'APH', 'ADI', 'ANSS', 'AON', 'APA', 'APO', 'AAPL', 'AMAT', 'APTV', 'ACGL', 'ADM',
    'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'AXON', 'BKR',
    'BALL', 'BAC', 'BAX', 'BDX', 'BBY', 'TECH', 'BIIB', 'BLK', 'BX', 'BK', 'BA', 'BKNG',
    'BWA', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BLDR', 'BG', 'BXP', 'CHRW', 'CDNS', 'CZR',
    'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE',
    'COR', 'CNC', 'CNP', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI',
    'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA',
    'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CPAY', 'CTVA', 'CSGP', 'COST',
    'CTRA', 'CRWD', 'CCI', 'CSX', 'CMI', 'CVS', 'DHR', 'DRI', 'DVA', 'DAY', 'DECK', 'DE',
    'DELL', 'DAL', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV',
    'DOW', 'DHI', 'DTE', 'DUK', 'DD', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'ELV',
    'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EQT', 'EFX', 'EQIX', 'EQR', 'ERIE', 'ESS', 'EL',
    'EG', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FICO', 'FAST',
    'FRT', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FI', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX',
    'BEN', 'FCX', 'GRMN', 'IT', 'GE', 'GEHC', 'GEV', 'GEN', 'GNRC', 'GD', 'GIS', 'GM', 'GPC', 'GILD',
    'GPN', 'GL', 'GDDY', 'GS', 'HAL', 'HIG', 'HAS', 'HCA', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT',
    'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX',
    'ITW', 'INCY', 'IR', 'PODD', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'INVH', 'IQV',
    'IRM', 'JBHT', 'JBL', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 'KEYS', 'KMB',
    'KIM', 'KMI', 'KKR', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LII', 'LLY',
    'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LULU', 'LYB', 'MTB', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS',
    'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'META', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA',
    'MRNA', 'MHK', 'MOH', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP',
    'NFLX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE',
    'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'ON', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PLTR',
    'PANW', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 'PEP', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PNC', 'POOL',
    'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PTC', 'PSA', 'PHM', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF',
    'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RVTY', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM',
    'SBAC', 'SLB', 'STX', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SJM', 'SW', 'SNA', 'SOLV', 'SO', 'LUV', 'SWK',
    'SBUX', 'STT', 'STLD', 'STE', 'SYK', 'SMCI', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TRGP',
    'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TPL', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV',
    'TRMB', 'TFC', 'TYL', 'TSN', 'USB', 'UBER', 'UDR', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO',
    'VTR', 'VLTO', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VTRS', 'VICI', 'V', 'VST', 'VMC', 'WRB', 'GWW', 'WAB', 'WBA',
    'WMT', 'DIS', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WY', 'WMB', 'WTW', 'WDAY', 'WYNN',
    'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZTS'
    ]

SOME_MORE = [
    "WMT", "WYNN", "XLB", "XBI", "XLF", "XLK", "XLY", "XLP", "XME",
    "XOM", "XOP", "XYL", "YUM", "ZBH", "ZION",
    "ZTS", "ZNGA", "ZMH", "ZTO", "AAL", "AAP", "ABBV", "ABT",
    "ACN", "ABFH", "AGNC", "AIG", "ALL", "ALXN",
    "ANTM", "AON", "APA", "APC", "APD", "APH", "ARE", "ARGO",
    "ARKG", "ARKK", "ARKQ", "ARKW", "ARMK", "ASIA", "ATVI",
    "AVY", "BABA", "BBBY", "BBT", "BBVA", "BCS", "BDX", "BEN", "BF.B",
    "BK", "BMY", "BRKB", "BSX",
    "TGT", "TWTR", "UA", "UNH", "UNM", "UNP", "UPS",
    "USB", "V", "VZ", "WAG", "WFC", "WHR", "WLTW", "WM", "WMB", "WMT",
    "IYW", "QQEW", "QQDM", "IHI", "IHD", "IHS", "IHO", "SPGI",
    "IGF", "IGI", "IGM", "IGV", "IGW", "IHY", "IJH", "IJR", "IJS", "IJV",
    "IYW", "IYZ", "JCI", "JPM", "JNJ", "JNPR", "K", "KEY", "KMI",
    "KMB", "KMI", "KMX", "KO", "CPRI", "KR", "KSS", "KSU", "L", "LB",
    "LEG", "LEN", "LEVI", "LFC", "LH", "LHX", "LIN", "LKQ", "LLY",
    "LMT", "LNC", "LNT", "LOW", "LUV", "LVS", "LYB", "M", "MA", "MAA",
    "MCD", "MCK", "MCO", "MDT", "MET", "MGM", "MHK", "MJN", "MKC", "MLM",
    "MMC", "MMM", "MNST", "MO", "AG", "MOS", "MPC", "MRK", "MRO", "MS",
    "RUN", "NEE", "CGC", "ACB", "TLEY", "CUR", "GTB", "U", "RBLX", "TTWC", 
    "NTD", "CRSP", "BNTX", "VST", "TEM"
    ]

ETF  = [
    "NLR", "URA", "XLE", "TOPT", "XLG", "GRNY", "MAGS", "IBIT", "HACK",
    "IGV", "SMH", "QQQM", "VOO", "IWM", "NDA", "FXI"
    ]



def get_stock_analysis(tickers):
    results = []
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)  # Ensure enough data for SMA calculations

    for ticker in tickers:
        try:
            # Fetch historical data
            data = yf.download(ticker, start=start_date, end=end_date)

            if data.empty:
                print(f"No data found for {ticker}")
                continue

            # Calculate SMAs
            data['SMA_50'] = data['Close'].rolling(window=50).mean()
            data['SMA_150'] = data['Close'].rolling(window=150).mean()
            data['SMA_200'] = data['Close'].rolling(window=200).mean()
            
            # Handle NaN values by filling forward and backward
            data['SMA_150'] = data['SMA_150'].ffill().bfill()
            data['SMA_50'] = data['SMA_50'].ffill().bfill()
            data['SMA_200'] = data['SMA_200'].ffill().bfill()

            # Get the most recent values using .item()
            latest_price = data['Close'].iloc[-1].item()
            latest_sma_50 = data['SMA_50'].iloc[-1].item()
            latest_sma_150 = data['SMA_150'].iloc[-1].item()
            latest_sma_200 = data['SMA_200'].iloc[-1].item()

            # Check if stock is within 5% range of SMA_150
            if latest_sma_150 <= latest_price <= (1.05 * latest_sma_150):
                # Check if the 150-day SMA is rising
                sma_150_previous = data['SMA_150'].iloc[-2].item()
                sma_150_ten_days_ago = data['SMA_150'].iloc[-10].item()
                
                is_rising_150 = (latest_sma_150 > sma_150_previous and 
                                sma_150_previous > sma_150_ten_days_ago)

                if is_rising_150:
                    # Check for "Gold Stock" or "Red Stock" criteria
                    recent_data = data.tail(10)

                    # Modified crossover checks to use .any().item()
                    crossed_gold = (
                        ((recent_data['SMA_50'] > recent_data['SMA_200']) &
                        (recent_data['SMA_50'].shift(1) <= recent_data['SMA_200'].shift(1))).any().item()
                    )
                    crossed_red = (
                        ((recent_data['SMA_50'] < recent_data['SMA_200']) &
                        (recent_data['SMA_50'].shift(1) >= recent_data['SMA_200'].shift(1))).any().item()
                    )

                    stock_label = ''
                    if crossed_gold:
                        stock_label = 'Gold Stock'
                    elif crossed_red:
                        stock_label = 'Red Stock'

                    results.append({
                        'Stock': ticker,
                        'Current Price': round(latest_price, 2),
                        'SMA_150': round(latest_sma_150, 2),
                        'Label': stock_label
                    })
                #     results.append({
                #         'Stock': ticker,
                #         'Current Price': latest_price,
                #         'SMA_50': latest_sma_50,
                #         'SMA_150': latest_sma_150,
                #         'SMA_200': latest_sma_200
                # })
        except Exception as e:
            print(f"Error processing {ticker}: {str(e)}")
            continue

    # Create and return a DataFrame from the results
    return pd.DataFrame(results)

list_of_stocks = [NSDK100, SP500, SOME_MORE, ETF]

for lst_stoks in list_of_stocks:
    # Get the results
    result_df = get_stock_analysis(lst_stoks)
    # Print the results
    print(tabulate(result_df, headers='keys', tablefmt='grid'))

