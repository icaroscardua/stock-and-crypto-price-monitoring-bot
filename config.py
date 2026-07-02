import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

ASSETS = [
    {"symbol": "AAPL", "min": 150.00, "max": 350.00},
    {"symbol": "BTC-USD", "min": 40000, "max": 80000},
]