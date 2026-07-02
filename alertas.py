import requests
from config import TELEGRAM_TOKEN, CHAT_ID

alerted = {}

def send_alert(symbol, price, threshold, direction):
    key = f"{symbol}-{direction}"

    if alerted.get(key):
        return

    alerted[key] = True

    variation = abs((price - threshold) / threshold * 100)

    if direction == "above":
        message = (
            f"🚀 Alert: {symbol}\n"
            f"Current price: ${price:.2f}\n"
            f"⬆️ Above maximum threshold of ${threshold:.2f}\n"
            f"📊 Variation: +{variation:.2f}%"
        )
    else:
        message = (
            f"🚨 Alert: {symbol}\n"
            f"Current price: ${price:.2f}\n"
            f"⬇️ Below minimum threshold of ${threshold:.2f}\n"
            f"📊 Variation: -{variation:.2f}%"
        )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

def reset_alert(symbol, direction):
    key = f"{symbol}-{direction}"
    alerted[key] = False