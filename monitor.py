import yfinance as yf

def search_price(symbol):
    try:
        active = yf.Ticker(symbol)
        price = active.fast_info["last_price"]
        return price
    except Exception as e:
        print(f"Couldn't fetch the price of {symbol}: {e}")
        return None 