import requests
from config import TELEGRAM_TOKEN, CHAT_ID

def send_alert(symbol, price, threshold, direction):
    if direction == "above":
        emoji = "🚀"
        message = f"{emoji} ALERT: {symbol}\nCurrent price: ${price:.2f}\n⬆️ Above maximum threshold of ${threshold:.2f}"
    else:
        emoji = "🚨"
        message = f"{emoji} ALERT: {symbol}\nCurrent price: ${price:.2f}\n⬇️ Below minimum threshold of ${threshold:.2f}"

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)