import time
import threading
from monitor import search_price
from alertas import send_alert, reset_alert
from config import ASSETS
from bot import start_bot

CHECK_INTERVAL = 300

def monitor():
    print("📈 Monitoring started!")
    while True:
        for asset in ASSETS:
            symbol = asset["symbol"]
            min_price = asset["min"]
            max_price = asset["max"]

            price = search_price(symbol)

            if price is None:
                continue

            print(f"{symbol}: ${price:.2f}")

            if price < min_price:
                send_alert(symbol, price, min_price, "below")
                reset_alert(symbol, "above")
            elif price > max_price:
                send_alert(symbol, price, max_price, "above")
                reset_alert(symbol, "below")
            else:
                reset_alert(symbol, "below")
                reset_alert(symbol, "above")

        print(f"⏳ Waiting {CHECK_INTERVAL} seconds...\n")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("🤖 Bot started!")
    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()
    start_bot()