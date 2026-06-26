# 📈 Stock & Crypto Price Monitor Bot

Automated bot built with Python that monitors stock and crypto prices in real time and sends instant alerts via Telegram when a target price is reached.

---

## 🚀 Features

- 📊 Real-time price monitoring for stocks and cryptocurrencies
- 📬 Instant Telegram alerts when a target price is hit
- 🔁 Supports multiple assets simultaneously
- ⚙️ Configurable price thresholds (min and max)
- 🛡️ Error handling for invalid assets and connection issues

---

## 🛠️ Technologies & Libraries

| Library | Purpose |
|---|---|
| `yfinance` | Fetches real-time market data for stocks and cryptos |
| `requests` | Handles HTTP requests |
| `python-telegram-bot` | Sends alert messages via Telegram |

---

## 📁 Project Structure

```
bot-monitoramento/
├── main.py         # Entry point — starts the monitoring loop
├── monitor.py      # Price fetching logic
├── alertas.py      # Alert conditions and notification logic
├── config.py       # Assets, thresholds, and Telegram credentials
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/bot-monitoramento.git
cd bot-monitoramento
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your assets and Telegram bot
Edit `config.py` with your settings:
```python
TELEGRAM_TOKEN = "your-telegram-bot-token"
CHAT_ID = "your-chat-id"

ASSETS = [
    {"symbol": "AAPL", "min": 150.00, "max": 200.00},
    {"symbol": "BTC-USD", "min": 60000, "max": 80000},
]
```

> 💡 To create a Telegram bot and get your token, talk to [@BotFather](https://t.me/BotFather) on Telegram.

### 5. Run the bot
```bash
python main.py
```

---

## 📬 Example Alert

```
🚨 Alert: AAPL
Current price: $148.30
⬇️ Below minimum threshold of $150.00
```

---

## 📌 Requirements

- Python 3.8+
- A Telegram account and bot token

---

## 🧠 Motivation

This project was built to put into practice Python fundamentals combined with automation concepts, using third-party libraries to interact with financial market data and messaging APIs.

---

## 📄 License

This project is licensed under the MIT License.
