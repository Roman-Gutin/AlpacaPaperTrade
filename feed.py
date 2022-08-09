from concurrent.futures import ThreadPoolExecutor
from alpaca_trade_api.stream import Stream, URL

ALPACA_KEYS = {
    'key': 'AK09KE1XGIXEKIOCUWEJ',
     "secret": 'oKYYBxJ427LPTEHJmjAaW24SdZv9KGejVbn3eqX3' }

ALPACA_API_KEY  , ALPACA_SECRET_KEY  = ALPACA_KEYS.values()

class QuoteFeed:
    thread_pool = ThreadPoolExecutor(2)
  
    def __init__(self,tickers):
        self.tickers = tickers
    
    def __del__(self):
        self.stop()
        del self.conn
    
    async def on_quote(self, q):
        ticker = q.symbol
        self.live_quotes[ticker] = q._raw
         
    def connect(self):
        self.conn = Stream(ALPACA_API_KEY,
                      ALPACA_SECRET_KEY,
                      base_url=URL('https://paper-api.alpaca.markets'),
                      data_feed='sip')


        self.live_quotes = {ticker:None for ticker in self.tickers}
        self.conn.subscribe_quotes(self.on_quote, *self.tickers) 
        self.conn.run()
        
    def stop(self):
        self.conn.stop()
    
    def start(self):
        self.thread_pool.submit(self.connect)
        
    
