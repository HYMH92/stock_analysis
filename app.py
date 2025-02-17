# app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import pickle
import os
from stock_analysis import get_stock_analysis, NSDK100, SP500, SOME_MORE, ETF

# Page configuration with a custom theme
st.set_page_config(
    page_title="MSA - 150",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 1rem;
            color: #1E88E5;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .sub-header {
            text-align: center;
            padding: 1.5rem;
            color: #424242;
            font-size: 1.2em;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
        }
        .last-update {
            padding: 0.5rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            text-align: center;
        }
        .stButton > button {
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
            display: block;
            background-color: #1E88E5;
            color: white;
        }
        .stock-status-gold {
            color: #FFD700;
            font-weight: bold;
        }
        .stock-status-red {
            color: #FF4444;
            font-weight: bold;
        }
        .tab-content {
            padding: 1rem;
            border-radius: 5px;
            background-color: #f8f9fa;
        }
    </style>
""", unsafe_allow_html=True)

# Header section with improved styling
st.markdown('<h1 class="main-header">📈 MSA - 150 Stock Analysis</h1>', unsafe_allow_html=True)

# Enhanced description
st.markdown("""
    <div class="sub-header">
        <p>Welcome to MSA-150, your daily stock market analysis tool! 🚀</p>
        <p>This tool identifies stocks that are showing promising technical patterns based on their 150-day moving average.</p>
        <p><strong>What we look for:</strong></p>
        <ul>
            <li>Stocks within 5% above their 150-day moving average</li>
            <li>Upward trend confirmation over the past week</li>
            <li>Special indicators for "Gold" and "Red" stock status</li>
        </ul>
        <p><em>Data refreshes daily at midnight to ensure you're working with the latest market information.</em></p>
    </div>
""", unsafe_allow_html=True)

# Function to check if we need to reset data
def should_reset_data():
    now = datetime.now()
    if now.hour == 0 and now.minute < 5:
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
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# Check if we need to reset
if should_reset_data():
    st.session_state.results = None
    st.session_state.last_update = None
    st.session_state.button_clicked = False
    if os.path.exists('stock_results.pkl'):
        os.remove('stock_results.pkl')

# Function to handle button click
def fetch_stocks():
    st.session_state.button_clicked = True
    with st.spinner("🔍 Analyzing market data..."):
        results = {}
        stock_groups = {
            "🎯 NASDAQ 100": NSDK100,
            "💫 S&P 500": SP500,
            "✨ Additional Stocks": SOME_MORE,
            "📊 ETFs": ETF
        }
        
        for group_name, stocks in stock_groups.items():
            df = get_stock_analysis(stocks)
            if not df.empty:
                results[group_name] = df
        
        st.session_state.results = results
        st.session_state.last_update = datetime.now()
        save_results(results)

# Function to check for updated data
def check_for_updates():
    if st.session_state.last_update is None or st.session_state.last_update.date() < datetime.now().date():
        fetch_stocks()
    else:
        st.info("Data is already up-to-date.")

# Display the "Find stocks" button if needed
if st.session_state.results is None and not st.session_state.button_clicked:
    st.markdown("<br>", unsafe_allow_html=True)  # Add some spacing
    st.button("🎯 Analyze Stocks", on_click=fetch_stocks)

# Display the "Check for updated data" button
st.button("🔄 Check for updated data", on_click=check_for_updates)

# Display results if available
if st.session_state.results is not None:
    # Show last update time with improved styling
    if st.session_state.last_update:
        st.markdown(
            f'<div class="last-update">🕒 Last updated: '
            f'{st.session_state.last_update.strftime("%Y-%m-%d %H:%M:%S")}</div>',
            unsafe_allow_html=True
        )
    
    # Create tabs for different stock groups with improved styling
    tabs = st.tabs(list(st.session_state.results.keys()))
    
    for tab, (group_name, df) in zip(tabs, st.session_state.results.items()):
        with tab:
            st.markdown('<div class="tab-content">', unsafe_allow_html=True)
            if not df.empty:
                # Add summary metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Stocks", len(df))
                with col2:
                    gold_stocks = len(df[df['Label'] == 'Gold Stock'])
                    st.metric("Gold Stocks", gold_stocks)
                with col3:
                    red_stocks = len(df[df['Label'] == 'Red Stock'])
                    st.metric("Red Stocks", red_stocks)

                # Enhanced dataframe display
                st.dataframe(
                    df,
                    column_config={
                        "Stock": st.column_config.TextColumn(
                            "Stock Symbol",
                            help="Trading symbol for the stock"
                        ),
                        "Current Price": st.column_config.NumberColumn(
                            "Current Price",
                            format="$%.2f",
                            help="Current trading price"
                        ),
                        "SMA_150": st.column_config.NumberColumn(
                            "150-day SMA",
                            format="$%.2f",
                            help="150-day Simple Moving Average"
                        ),
                        "Label": st.column_config.TextColumn(
                            "Stock Status",
                            help="Indicates if the stock is showing Gold or Red patterns"
                        )
                    },
                    hide_index=True,
                    use_container_width=True
                )
            else:
                st.info("No stocks matching criteria in this group")
            st.markdown('</div>', unsafe_allow_html=True)

# Add footer with additional information
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>💡 <strong>Tip:</strong> Check back daily for updated stock analysis!</p>
        <p style='font-size: 0.8em;'>Data provided by Yahoo Finance</p>
    </div>
""", unsafe_allow_html=True)