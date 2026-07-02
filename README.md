# 📈 Stock & Crypto Price Monitor Bot

Automated bot built with Python that monitors stock and crypto prices in real time and sends instant alerts via Telegram when a target price is reached. Assets and thresholds can be managed directly through Telegram commands — no code editing required.

---

## 🚀 Features

- 📊 Real-time price monitoring for stocks and cryptocurrencies
- 📬 Instant Telegram alerts when a target price is hit
- 🔁 Supports multiple assets simultaneously
- ⚙️ Manage assets directly via Telegram commands
- 🔕 Smart alert deduplication — no repeated notifications for the same event
- 📉 Percentage variation displayed in every alert
- 🛡️ Error handling for invalid assets and connection issues

---

## 🤖 Telegram Commands

| Command | Description | Example |
|---|---|---|
| `/start` | Welcome message and instructions | `/start` |
| `/add SYMBOL MIN MAX` | Add an asset to monitor | `/add AAPL 150 350` |
| `/update SYMBOL MIN MAX` | Update thresholds of an asset | `/update AAPL 200 400` |
| `/remove SYMBOL` | Remove an asset | `/remove AAPL` |
| `/list` | List all monitored assets | `/list` |

---

## 📬 Example Alert
```
🚨 Alert: BTC-USD
Current price: $58500.00
⬇️ Below minimum threshold of $60000.00
📊 Variation: -2.50%
``` 

---

## 🛠️ Technologies & Libraries

| Library | Purpose |
|---|---|
| `yfinance` | Fetches real-time market data for stocks and cryptos |
| `requests` | Handles HTTP requests |
| `python-telegram-bot` | Sends alerts and handles commands via Telegram |
| `threading` | Runs monitoring and bot in parallel |

---

## 📁 Project Structure

```
stock-and-crypto-price-monitoring-bot/
├── main.py             # Entry point — starts monitoring and bot in parallel
├── monitor.py          # Price fetching logic
├── alertas.py          # Alert conditions, deduplication and notification logic
├── bot.py              # Telegram command handlers
├── config.py           # Assets, thresholds and Telegram credentials (not versioned)
├── config.example.py   # Example configuration file
├── requirements.txt
└── README.md
```
---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/icaroscardua/stock-and-crypto-price-monitoring-bot.git
cd stock-and-crypto-price-monitoring-bot
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

### 4. Configure your credentials
Copy `config.example.py` to `config.py`:
```bash
copy config.example.py config.py
```

Create a `.env` file in the root of the project:
```bash
New-Item .env
```

And fill in your credentials:

```
TELEGRAM_TOKEN = "your-telegram-bot-token"
CHAT_ID = your-chat-id
```

> 💡 To create a Telegram bot and get your token, talk to [@BotFather](https://t.me/BotFather) on Telegram.
> 💡 To get your Chat ID, send a message to your bot and access: `https://api.telegram.org/botYOUR_TOKEN/getUpdates`

### 5. Run the bot
```bash
python main.py
```

---

## 📌 Requirements

- Python 3.8+
- A Telegram account and bot token

---

## 🧠 Motivation

This project was built to put into practice Python fundamentals combined with automation and real-world API integration, using third-party libraries to interact with financial market data and the Telegram messaging platform.

---

## 📄 License

This project is licensed under the MIT License.