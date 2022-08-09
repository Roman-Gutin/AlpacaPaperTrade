import streamlit as st
import pandas as pd
from feed import QuoteFeed
tickers = ['SQQQ']
feed = QuoteFeed(tickers)
st.title('LETF Paper Trade Dashboard')
feed.start()

class QuoteMetric:
    fields = ['bid_price', 'ask_price']
    
    def __init__(self, ticker):
        self.metrics = dict(zip(self.fields, st.columns(len(self.fields))))
        self.ticker = ticker
        self.last_quote = None
                            
        for col_name, column in self.metrics.items():
            with column:
                st.header(self.ticker)
                st.metric(col_name, "0", "0")
                            
                            
    def update(self, quote):
        for col_name, column in self.metrics.items:
            with column:
                st.header(self.ticker)
                st.metric(
                       label = col_name, 
                       value = quote[col_name], 
                       delta = self._delta(quote, col_name)
                   )
        
    def _delta(self,quote, field):
        delta = (quote[field]-self.last_quote[field])/self.last_quote[field]
        self.last_quote = quote
        return f'{delta*100} bps'
                                                          
                            
                                                          
                            
latest_quotes = {ticker:QuoteMetric(ticker) for ticker in tickers}

while True:
    for ticker, quote in feed.live_quotes.items():
         latest_quotes [ticker].update(quote)


                                
