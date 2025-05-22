import os
import asyncio
import requests
from threading import Thread
from prometheus_client import start_http_server, Counter
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
import os
import asyncio
from threading import Thread
from prometheus_client import Counter, start_http_server
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters,
)

messages_received = Counter("telegram_messages_received_total", "Total number of received messages")
commands_received = Counter("telegram_commands_received_total", "Total number of received commands")

async def start(update: Update, context: CallbackContext):
    commands_received.inc()
    await update.message.reply_text("Hi")

async def echo(update: Update, context: CallbackContext):
    if not (update.message and update.message.from_user and update.message.text):
        return

    messages_received.inc()

    await update.message.reply_text(f"You sent: {update.message.text}")

async def error_handler(update: object, context: CallbackContext):
    print("[ERROR]", context.error)

def start_metrics_server(port=8000):
    print(f"Starting Prometheus metrics server on port {port}...")
    start_http_server(port)

def main():
    Thread(target=start_metrics_server, daemon=True).start()

    token = os.getenv("TELEGRAM_TOKEN", "")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_error_handler(error_handler)

    print("Bot is starting...")
    app.run_polling()
    print("Bot stopped.")

if __name__ == "__main__":
    main()
