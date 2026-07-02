from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN, ASSETS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Stock & Crypto Monitor Bot!\n\n"
        "Available commands:\n"
        "/add SYMBOL MIN MAX — Add an asset to monitor\n"
        "/update SYMBOL MIN MAX - Update min and max of an asset\n"
        "/remove SYMBOL — Remove an asset\n"
        "/list — List all monitored assets\n"
        "Bot by Ícaro Scárdua"
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper()
        min_price = float(context.args[1])
        max_price = float(context.args[2])

        for asset in ASSETS:
            if asset["symbol"] == symbol:
                await update.message.reply_text(f"⚠️ {symbol} is already being monitored!")
                return

        ASSETS.append({"symbol": symbol, "min": min_price, "max": max_price})
        await update.message.reply_text(f"✅ {symbol} added!\nMin: ${min_price:.2f} | Max: ${max_price:.2f}")

    except (IndexError, ValueError):
        await update.message.reply_text("❌ Invalid format. Use: /add SYMBOL MIN MAX\nExample: /add AAPL 150 350")

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper()

        for asset in ASSETS:
            if asset["symbol"] == symbol:
                ASSETS.remove(asset)
                await update.message.reply_text(f"✅ {symbol} removed successfully!")
                return

        await update.message.reply_text(f"⚠️ {symbol} not found in monitoring list.")

    except IndexError:
        await update.message.reply_text("❌ Invalid format. Use: /remove SYMBOL\nExample: /remove AAPL")

async def list_assets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ASSETS:
        await update.message.reply_text("📭 No assets being monitored.")
        return

    message = "📊 Monitored assets:\n\n"
    for asset in ASSETS:
        message += f"• {asset['symbol']} | Min: ${asset['min']:.2f} | Max: ${asset['max']:.2f}\n"

    await update.message.reply_text(message)

async def update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper()
        min_price = float(context.args[1])
        max_price = float(context.args[2])

        for asset in ASSETS:
            if asset["symbol"] == symbol:
                asset["min"] = min_price
                asset["max"] = max_price
                await update.message.reply_text(
                    f"✅ {symbol} updated!\n"
                    f"New Min: ${min_price:.2f} | New Max: ${max_price:.2f}"
                )
                return

        await update.message.reply_text(f"⚠️ {symbol} not found. Use /add to add it first.")

    except (IndexError, ValueError):
        await update.message.reply_text("❌ Invalid format. Use: /update SYMBOL MIN MAX\nExample: /update AAPL 200 400")

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("remove", remove))
    app.add_handler(CommandHandler("list", list_assets))
    app.add_handler(CommandHandler("update", update))
    app.run_polling()