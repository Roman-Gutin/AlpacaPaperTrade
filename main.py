import streamlit as st
import pandas as pd
from feed import QuoteFeed
tickers = ['SQQQ']

st.title('LETF Paper Trade Dashboard')

ticker_columns = dict(zip(tickers, st.columns(len(tickers))))
                          
for ticker, column in ticker_columns.items():
    with column:
        st.header(ticker)
        st.text('999')
        st.text('9991')   
