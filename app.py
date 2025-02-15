# app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import pickle
import os
from stock_analysis import get_stock_analysis, NSDK100, SP500, SOME_MORE, ETF

# Page configuration
st.set_page_config(
    page_title="MSA - 150",
    page_icon="📈",
    layout="wide"
)

# Title and subtitle
st.title("MSA - 150")
st.markdown("### On this page you can find the list of stocks that are within five percent (above) of their average of 150, and also in an upward trend over the past week")

# Function to check if we need to reset data
def should_reset_data():
    now = datetime.now()
    if now.hour == 0 and now.minute < 5:  # Check if it's midnight (with 5-minute buffer)
        return True
    return False

# Function to save results
def save_results(results):
    with open('stock_results.pkl', 'wb') as f:
        pickle.dump(results, f)

# Function to load results
def load_results():
    try:
        with open('stock_results.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None

# Initialize session state
if 'last_update' not in st.session_state:
    st.session_state.last_update = None
if 'results' not in st.session_state:
    st.session_state.results = load_results()

# Check if we need to reset
if should_reset_data():
    st.session_state.results = None
    st.session_state.last_update = None
    if os.path.exists('stock_results.pkl'):
        os.remove('stock_results.pkl')

# Display the "Find stocks" button if needed
if st.session_state.results is None:
    if st.button("Find Stocks"):
        with st.spinner("Analyzing stocks..."):
            results = {}
            stock_groups = {
                "NASDAQ 100": NSDK100,
                "S&P 500": SP500,
                "Additional Stocks": SOME_MORE,
                "ETFs": ETF
            }
            
            for group_name, stocks in stock_groups.items():
                df = get_stock_analysis(stocks)
                if not df.empty:
                    results[group_name] = df
            
            st.session_state.results = results
            st.session_state.last_update = datetime.now()
            save_results(results)
            st.experimental_rerun()

# Display results if available
if st.session_state.results is not None:
    # Show last update time
    if st.session_state.last_update:
        st.info(f"Last updated: {st.session_state.last_update.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create tabs for different stock groups
    tabs = st.tabs(list(st.session_state.results.keys()))
    
    for tab, (group_name, df) in zip(tabs, st.session_state.results.items()):
        with tab:
            if not df.empty:
                st.dataframe(
                    df,
                    column_config={
                        "Stock": st.column_config.TextColumn("Stock Symbol"),
                        "Current Price": st.column_config.NumberColumn(
                            "Current Price",
                            format="$%.2f"
                        ),
                        "SMA_150": st.column_config.NumberColumn(
                            "150-day SMA",
                            format="$%.2f"
                        ),
                        "Label": st.column_config.TextColumn("Stock Status")
                    },
                    hide_index=True,
                    use_container_width=True
                )
            else:
                st.write("No stocks matching criteria in this group")
